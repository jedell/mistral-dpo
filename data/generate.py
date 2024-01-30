from dotenv import load_dotenv
import os
from client import GooglePlacesClient

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
    
client = GooglePlacesClient(api_key=api_key)
location = {"latitude": 37.7937, "longitude": -122.3965}
radius = 500.0 # meters
types = ["restaurant"]
response = client.search_nearby(location, radius, types)
print(response)

# messages = [
#     {"role": "system", "content": "You are Hermes 2."},
#     {"role": "user", "content": "Hello, who are you?"}
# ]

# <|im_start|>system
# You are an AI assistant capable of interacting with the Google Places API. 
# You can call the 'search_nearby' and 'search_text' functions with parameters like 'location', 'radius', 'types', and 'additional_fields'. You can use fields like 'places.allowsDogs', 'places.outdoorSeating', etc. to refine the search. Your goal is to provide the best places that answer the user's query.