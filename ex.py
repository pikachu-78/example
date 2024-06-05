import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_file", required=True)
args = parser.parse_args()
changed_file = args.changed_file

print("Changed file:", changed_file)  # Add this line for debugging

def main(file_path):
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
    main(changed_file)
