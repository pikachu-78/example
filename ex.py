import json
import argparse
import os
import requests

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_file")  # Expecting a single comma-separated string
args = parser.parse_args()
changed_files = args.changed_file.split()  # Split the input string on whitespace
# token = os.getenv('TOKEN')
token = "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"  # Use if not using environment variable
print("Token:", token)

print("Changed files:", changed_files)

github_headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}
owner = "pikachu-78"
repo = "example"
name = "456"

github_api = f'https://api.github.com/repos/{owner}/{repo}/branches/{name}'
print("GitHub API URL:", github_api)  # Debugging output

try:
    response = requests.get(github_api, headers=github_headers)
    response.raise_for_status()
    file_content = response.json()
    print(file_content)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

def main(file_paths):
    for file_path in file_paths:
        try:
            with open(file_path) as json_file:
                teams = json.load(json_file)
                for team_data in teams:
                    print(team_data['name'])
                    print(team_data['roll'])
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except json.JSONDecodeError:
            print(f"File {file_path} is not a valid JSON file")

if __name__ == "__main__":
    main(changed_files)
