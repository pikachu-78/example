import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_files", default="conf/**")
args = parser.parse_args()
changed_files = args.changed_files

def main(file_paths=None):
    if file_paths is None:
        print("No file paths provided.")
        return
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
    if len(changed_files) != 1:
        main()
    else:
        main(changed_files)
