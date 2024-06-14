import json
import argparse

def update_name_by_roll(changed_files, roll_to_update, new_name):
    try:
        with open(changed_files) as json_file:
            teams = json.load(json_file)
            for team_data in teams:
                if team_data['roll'] == roll_to_update:
                    team_data['name'] = new_name
        # Write the updated data back to the file
        with open(changed_files, 'w') as json_file:
            json.dump(teams, json_file, indent=4)
    except FileNotFoundError:
        print(f"File {changed_files} not found")
    except json.JSONDecodeError:
        print(f"File {changed_files} is not a valid JSON file")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--changed_file")  # Expecting a single file path
args = parser.parse_args()
changed_files = args.changed_file

# Define roll and new name to update
roll_to_update = "oneiii-2"
new_name = "Updated Name"

# Update name based on roll
update_name_by_roll(changed_files, roll_to_update, new_name)
