from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

import json
import random
from openai import OpenAI
from place_types import PlaceTypes
from fields import Fields
from prompts import generate_prompt
import inspect
from client import validate_search_input

with open('data/fixed_samples.json', 'r') as file:
    existing_samples = json.load(file)
print(f"Current length of existing samples: {len(existing_samples)}")
with open('data/fixed_gpt3_samples.json', 'r') as file:
    new_gen_samples = json.load(file)
print(f"Current length of gpt3 samples: {len(new_gen_samples)}")

place_types = list(filter(lambda x: x is not None, [member[1] if '__' not in member[0] else None for member in inspect.getmembers(PlaceTypes)]))
fields = list(filter(lambda x: x is not None, [member[1] if '__' not in member[0] else None for member in inspect.getmembers(Fields)]))

def prepare_prompt(samples, place_types, fields, num_samples=3, num_place_types=10, num_fields=40):
    sample_prompt = random.sample(samples, min(num_samples, len(samples)))
    place_type_prompt = random.sample(place_types, min(num_place_types, len(place_types)))
    field_prompt = random.sample(fields, min(num_fields, len(fields)))
    
    prompt = generate_prompt + "Generate 15 unique photo-related samples based on the format of the following examples. Be creative and try to generate samples that are unique and high-quality. Additionally, generate realistic and natural user queries that could be uttered in normal speech. Ensure user queries are for realistic scenarios. Important: User queries should in some way be dependent on photos of the place. That is, the user query can only be answered if photos of the location are returned, i.e 'Can you find a bar with lots of seating?', 'Can you find a park with lots of trees', 'Can you find a resturant that is close to the street?' etc. Please vary the location latitudes and longitudes used corresponding to various urban areas in the United States. Please use the selected place types and fields where they make logical sense according to the user query. Try to combine fields (along with the places.photos field) and places in complex, unique, but realistic ways so that the response contains information relevent to the user query:\n"
    pic_prompt = """
    Here are example user queries that rely on photo data to be answered correctly:
    Can you find a café with a cozy, vintage decor?
    Is there outdoor seating available at this restaurant?
    Show me restaurants that offer a scenic sea view.
    Find me a bar that's not too crowded on weekends.
    Does this shopping mall have ample parking space?
    Locate a library with wheelchair access.
    I'm looking for a spacious yoga studio.
    Show me what the sushi platter looks like at this Japanese restaurant.
    Find a pub that hosts live music nights.
    Can you find hotels close to the Eiffel Tower with a view from the room?
    Are there any parks with safe play areas for toddlers?
    Find me museums with modern art exhibits.
    Is there a gym with a swimming pool and sauna?
    Show me buildings with Gothic architecture in the area.
    Can you find hotel rooms with a modern interior design?
    I need a venue with a large, open floor plan for an event."
    Find me landmarks with historical significance in the city.
    Show me parks with waterfalls or natural springs.
    Are there any public art installations or sculptures nearby?
    Find me neighborhoods known for their vibrant street art.
    I'm looking for boutiques with a unique fashion selection.
    Show me cafes that serve visually appealing desserts.
    Find bars with interesting lighting or neon signs.
    Which restaurants are decorated for the holiday season?
    I want to see themed cafes, like cat cafes or ones with a literary theme.
    Show me campsites with kayaking or paddleboarding options.
    Are there any visible safety measures in place at any public swimming pools nearby?

    All the user queries you generate should require access to photos from the returned locations.
    """
    prompt += pic_prompt
    prompt += "Place Types:\n" + json.dumps(place_type_prompt, indent=2) + "\n"
    prompt += "Fields: \n" + json.dumps(field_prompt + ['places.photos'], indent=2) + "\n"
    prompt += json.dumps(sample_prompt, indent=2) + "\n"
    prompt += "New samples:\n"
    
    return prompt

def parse_generated_text(text):
    try:
        json_objects = json.loads(text)
        print("Parsed JSON objects successfully.")
        return json_objects
    except json.JSONDecodeError as e:
        print(f"Attempting to extract complete JSON objects from partial data due to decode error: {e}")
        try:
            # Attempt to manually parse the string to extract complete JSON objects
            complete_objects = []
            buffer = ""
            depth = 0
            for char in text:
                if char == '{':
                    depth += 1
                if depth > 0:
                    buffer += char
                if char == '}':
                    depth -= 1
                    if depth == 0:
                        # Attempt to parse the buffered object
                        try:
                            complete_objects.append(json.loads(buffer))
                            buffer = ""  # Reset buffer after successfully parsing an object
                        except json.JSONDecodeError:
                            print("Failed to parse an object within the text. Skipping.")
            print(f"Recovered {len(complete_objects)} complete JSON objects from partial data.")
            return complete_objects
        except Exception as e:
            print(f"Failed to extract JSON objects due to an unexpected error: {e}")
            return []

openai_api = OpenAI(api_key=api_key)
# prompt = prepare_prompt(existing_samples, place_types, fields)

desired_new_samples_count = 100 
new_samples_collected = 0

while new_samples_collected < desired_new_samples_count:    
    try:
        prompt = prepare_prompt(existing_samples, place_types, fields)
        response = openai_api.chat.completions.create(model="gpt-4-0125-preview", messages=[{"role": "user", "content": prompt}])
        print(response)
        generated_samples = parse_generated_text(response.choices[0].message.content)
        
        verified_samples = []
        for sample in generated_samples:
            if isinstance(sample, dict):
                sample_json_str = sample['assistant'].replace("<|api_call|>", "").replace("<|api_call_end|>", "")
                sample_json = json.loads(sample_json_str)
                function_name = sample_json['function']
                if function_name in ['search_nearby', 'search_text']:
                    valid, error_message = validate_search_input(function_name, sample_json['parameters'])
                    if valid:
                        verified_samples.append(sample)
                        new_samples_collected += 1
                        if new_samples_collected >= desired_new_samples_count:
                            break
                    else:
                        print(f"Sample validation failed: {error_message}")
                else:
                    print("No valid function name found in sample.")
        
        new_gen_samples.extend(verified_samples)
        
        with open('data/fixed_gpt3_samples.json', 'w') as file:
            json.dump({"samples": new_gen_samples}, file, indent=2)
        
        print(f"Appended {len(verified_samples)} new samples. Total collected: {new_samples_collected}/{desired_new_samples_count}")
    
    except Exception as e:
        print(f"An error occurred during sample generation or validation: {e}")
        # TODO retry ?
