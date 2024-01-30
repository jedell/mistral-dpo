import json
from client import GooglePlacesClient
from dotenv import load_dotenv
import os
from client import GooglePlacesClient

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
    
def execute_api_call(api_call):
    client = GooglePlacesClient(api_key=api_key)
    function = getattr(client, api_call['function'])
    result = function(**api_call['parameters'])
    return result

import os

def main():
    base_dir = os.path.dirname(__file__)
    samples_file_path = os.path.join(base_dir, 'samples.json')
    successful_samples_file_path = os.path.join(base_dir, 'successful_samples.json')
    failed_samples_file_path = os.path.join(base_dir, 'failed_samples.json')

    with open(samples_file_path, 'r') as f:
        data = json.load(f)

    successful_samples = []
    failed_samples = []

    for sample in data['samples']:
        api_call = json.loads(sample['assistant'].split('<|api_call|>')[-1].split('<|api_call_end|>')[0])
        try:
            result, status = execute_api_call(api_call)
            if status // 100 == 2:
                print("Result:", status)
                successful_samples.append(sample)
            else:
                raise Exception(result)
        except Exception as e:
            sample['error'] = str(e)
            print('Error:', sample['error'])
            failed_samples.append(sample)

    with open(successful_samples_file_path, 'w') as f:
        json.dump(successful_samples, f)

    with open(failed_samples_file_path, 'w') as f:
        json.dump(failed_samples, f)

if __name__ == "__main__":
    main()