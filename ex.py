import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_file")  # Expecting a single comma-separated string
args = parser.parse_args()
changed_files = args.changed_file
  # Splitting the string into a list

print("Changed files:", changed_files)  # Add this line for debugging

def main(file_paths):
    # if len(file_paths) > 1:
    #     print("Only one file needs to be changed. Please specify only one file.")
    #     return    
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
