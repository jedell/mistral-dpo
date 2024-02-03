import json
from data.fields import Fields

def validate_and_update_fields(samples_file_path):
    with open(samples_file_path, 'r') as file:
        samples = json.load(file)
    samples = samples
    unique_fields = set()
    for sample in samples:
        assistant_data = json.loads(sample['assistant'].replace('<|api_call|>', "").replace('<|api_call_end|>', ""))
        if 'additional_fields' in assistant_data['parameters']:
            additional_fields = assistant_data['parameters']['additional_fields']        
            unique_fields.update(additional_fields)
        else:
            continue
    
    updated_fields = []
    for field in unique_fields:
        if not field.startswith("places."):
            field = "places." + field
        # Check if field exists in Fields class
        if hasattr(Fields, field.split('.')[1]):
            updated_fields.append(field)
        else:
            print(f"Field {field} does not exist in Fields class.")
    
    for sample in samples:
        assistant_data = json.loads(sample['assistant'].replace('<|api_call|>', "").replace('<|api_call_end|>', ""))
        if 'additional_fields' in assistant_data['parameters']:
            additional_fields = assistant_data['parameters']['additional_fields']        
        else:
            continue
        updated_additional_fields = []
        for field in additional_fields:
            if not field.startswith("places."):
                field = "places." + field
            if field in updated_fields:
                updated_additional_fields.append(field)
        original_str = sample['assistant'].split('\"additional_fields\": [')[1].split(']')[0]
        new_str = ", ".join([f"\"{field}\"" for field in updated_additional_fields])
        sample['assistant'] = sample['assistant'].replace(original_str, new_str)
    
    with open('data/results/FINAL_samples.json', 'w') as file:
        json.dump(samples, file, indent=4)

# validate_and_update_fields('data/results/FINAL_samples.json')

import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai_api = AsyncOpenAI(api_key=api_key)

async def async_prompt_openai_for_sensibility(sample):
    user_query = sample['user']
    response = await openai_api.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "The following question is related to a hypothetical system where a user can prompt a LLM about place and location information."},
            {"role": "user", "content": f"Yes or No: Is the following user query sensical and realistic? \"{user_query}\""}
        ],
    )
    if "yes" in response.choices[0].message.content.lower():
        return 'yes', sample
    else:
        return 'no', sample

async def prompt_openai_for_sensibility(samples_file_path):
    with open(samples_file_path, 'r') as file:
        samples = json.load(file)
    samples = samples

    tasks = [async_prompt_openai_for_sensibility(sample) for sample in samples]
    responses = await asyncio.gather(*tasks)

    yes_responses = [sample for response, sample in responses if response == 'yes']
    no_responses = [sample for response, sample in responses if response == 'no']

    return {'yes_responses': yes_responses, 'no_responses': no_responses}

async def sensibility_results():
    sensibility_results = await prompt_openai_for_sensibility('data/fixed_samples.json')
    with open('data/sensibility_results.json', 'w') as file:
        json.dump(sensibility_results, file, indent=4)

# asyncio.run(sensibility_results())


def count_samples_in_files():
    files = ['data/results/FINAL_samples.json']
    total_samples = 0
    for file_path in files:
        with open(file_path, 'r') as file:
            samples = json.load(file)
            total_samples += len(samples)
    print(f"Total samples in final_gpt3_samples.json and final_gpt4_samples.json: {total_samples}")

count_samples_in_files()

from client import validate_search_input

def validate_final_samples():
    with open('data/results/FINAL_samples.json', 'r') as file:
        gpt3_samples = json.load(file)

    final_samples = gpt3_samples #+ gpt4_samples['samples']
    valid_samples = []
    invalid_samples = []

    for sample in final_samples:
        sample_json_str = sample['assistant'].replace("<|api_call|>", "").replace("<|api_call_end|>", "")
        try:
            sample_json = json.loads(sample_json_str)
            function_name = sample_json['function']
            parameters = sample_json['parameters']
            valid, error_message = validate_search_input(function_name, parameters)
            if valid:
                valid_samples.append(sample)
            else:
                invalid_samples.append((sample, error_message))
        except json.JSONDecodeError as e:
            invalid_samples.append((sample, f"JSON decode error: {e}"))

    print(f"Total valid samples: {len(valid_samples)}")
    print(f"Total invalid samples: {len(invalid_samples)}")

    # Optionally, save the valid and invalid samples to files for further inspection
    with open('data/results/FINAL_valid_samples.json', 'w') as file:
        json.dump({"samples": valid_samples}, file, indent=4)
    with open('data/results/FINAL_invalid_samples.json', 'w') as file:
        json.dump({"samples": invalid_samples}, file, indent=4)

validate_final_samples()




