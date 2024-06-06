import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_file")  # Expecting a single comma-separated string
args = parser.parse_args()
changed_files = args.changed_file  # Split the input string on whitespace

print("Changed files:", changed_files)  # Add this line for debugging

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
    if len(changed_files) > 1:
        print(len(changed_files))
        print("Multiple changed files detected. Exiting without running main function.")
    else:
        main(changed_files)
