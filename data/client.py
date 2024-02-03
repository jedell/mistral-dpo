import requests
import json
from fields import Fields
from data.place_types import PlaceTypes
import inspect

class GooglePlacesClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://places.googleapis.com/v1/"
        self.base_headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.api_key
        }

    # TODO handle places.servesDesserts :P O>

    def _join_fields(self, base_fields, additional_fields):
        return ','.join([Fields.parse_field(field) if isinstance(field, str) else field.value for field in base_fields] + additional_fields)

    def _get(self, endpoint, headers):
        response = requests.get(self.base_url + endpoint, headers=headers)
        status = response.status_code if 'status_code' in response.__attrs__ else response.json()['error']['code']
        return response.json(), status

    def _post(self, endpoint, headers, data):
        response = requests.post(self.base_url + endpoint, headers=headers, data=json.dumps(data))
        status = response.status_code if 'status_code' in response.__attrs__ else response.json()['error']['code']
        return response.json(), status

    def search_nearby(self, location, radius, types, additional_fields=[], max_result_count=10):
        endpoint = "places:searchNearby"
        headers = self.base_headers.copy()
        base_fields = [Fields.id, Fields.displayName, Fields.formattedAddress, Fields.editorialSummary, Fields.types, Fields.websiteUri]
        headers['X-Goog-FieldMask'] = self._join_fields(base_fields, additional_fields)
        data = {
            "includedTypes": types,
            "maxResultCount": max_result_count,
            "locationRestriction": {
                "circle": {
                    "center": location,
                    "radius": radius
                }
            }
        }
        return self._post(endpoint, headers, data)

    def search_text(self, query, location, radius, additional_fields=[]):
        endpoint = "places:searchText"
        headers = self.base_headers.copy()
        base_fields = [Fields.id, Fields.displayName, Fields.formattedAddress, Fields.types, Fields.editorialSummary, Fields.websiteUri]
        headers['X-Goog-FieldMask'] = self._join_fields(base_fields, additional_fields)
        data = {
            "textQuery": query,
            "locationBias": {
                "circle": {
                    "center": location,
                    "radius": radius
                }
            }
        }
        return self._post(endpoint, headers, data)

    def place_details(self, place_id, additional_fields=[]):
        endpoint = f"places/{place_id}"
        headers = self.base_headers.copy()
        base_fields = [Fields.name, Fields.address, Fields.phoneNumber, Fields.websiteUri]
        headers['X-Goog-FieldMask'] = self._join_fields(base_fields, additional_fields)

        return self._get(endpoint, headers)
    
def validate_search_input(function_name, parameters):
    """
    Validates the inputs for the search_nearby and search_text functions.

    Args:
        function_name (str): The name of the function being validated ('search_nearby' or 'search_text').
        parameters (dict): The parameters passed to the function.

    Returns:
        bool: True if the inputs are valid, False otherwise.
        str: An error message if the inputs are invalid, otherwise an empty string.
    """
    valid_functions = ['search_nearby', 'search_text']
    if function_name not in valid_functions:
        return False, f"Invalid function name. Expected one of {valid_functions}, got '{function_name}'."

    if 'location' not in parameters or not isinstance(parameters['location'], dict):
        return False, "Missing or invalid 'location'. 'location' must be a dictionary with 'latitude' and 'longitude' keys."
    if 'latitude' not in parameters['location'] or not isinstance(parameters['location']['latitude'], (int, float)):
        return False, "Invalid 'latitude' in 'location'. 'latitude' must be a number."
    if 'longitude' not in parameters['location'] or not isinstance(parameters['location']['longitude'], (int, float)):
        return False, "Invalid 'longitude' in 'location'. 'longitude' must be a number."

    if function_name == 'search_nearby':
        if 'radius' not in parameters or not isinstance(parameters['radius'], (int, float)):
            return False, "Missing or invalid 'radius'. 'radius' must be a number."
        if 'types' in parameters and isinstance(parameters['types'], list):
            valid_types = [value for attr, value in inspect.getmembers(PlaceTypes) if not attr.startswith("__")]
            for item in parameters['types']:
                if item not in valid_types:
                    return False, f"Invalid 'type' value. '{item}' is not a recognized place type."

    if function_name == 'search_text':
        if 'query' not in parameters or not isinstance(parameters['query'], str):
            return False, "Missing or invalid 'query'. 'query' must be a string."
        if 'radius' in parameters and not isinstance(parameters['radius'], (int, float)):
            return False, "Invalid 'radius'. If provided, 'radius' must be a number."

    # Additional fields validation is optional for both functions
    if 'additional_fields' in parameters:
        if not isinstance(parameters['additional_fields'], list):
            return False, "Invalid 'additional_fields'. If provided, 'additional_fields' must be a list of strings."
        else:
            for field in parameters['additional_fields']:
                if Fields.parse_field(field) == "Unknown Field":
                    return False, f"Invalid field '{field}' in 'additional_fields'. The field does not exist."

    return True, ""
