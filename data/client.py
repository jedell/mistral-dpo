import requests
import json
from fields import Fields

class GooglePlacesClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://places.googleapis.com/v1/"
        self.base_headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.api_key
        }

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
        base_fields = [Fields.displayName, Fields.formattedAddress, Fields.types, Fields.websiteUri]
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
        base_fields = [Fields.displayName, Fields.formattedAddress]
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
