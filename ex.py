import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_files", default="conf/**", help="Space-separated list of changed JSON files")
args = parser.parse_args()
changed_files = args.changed_files

def process_file(file_path):
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

def main(changed_files):
    jfile_list = changed_files.split(" ")
    for file_path in jfile_list:
        process_file(file_path)

if __name__ == "__main__":
    main(changed_files)

