import json

def update_json(filename, roll, new_name):
    with open(filename, 'r') as file:
        data = json.load(file)

    for entry in data:
        if entry['roll'] == roll:
            entry['name'] = new_name

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    filename = "conf/team.json"
    roll = "oneiii-1"  # Change this to the roll you want to update
    new_name = "New"  # Change this to the new name you want to set
    update_json(filename, roll, new_name)
