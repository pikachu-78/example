import json
import jsonschema
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--changed_file")  # Expecting a single comma-separated string
args = parser.parse_args()
changed_files = args.changed_file.split()  # Split the input string on whitespace

print("Changed files:", changed_files)

# Custom validation function for 'isNotEmpty'
def validate_is_not_empty(validator, isNotEmpty, instance, schema):
    if isinstance(instance, (str, int, float, list, dict)):  # Include types you want to validate
        if isinstance(instance, str) and instance.strip() == "":
            yield jsonschema.ValidationError("Value must not be empty")
        elif isinstance(instance, (int, float)) and instance == "":
            yield jsonschema.ValidationError("Value must not be empty")
    else:
        return  # Skip validation for other types


# Registering the custom keyword 'isNotEmpty'
jsonschema.Draft7Validator.VALIDATORS['isNotEmpty'] = validate_is_not_empty

def validate_json(json_data, schema_data):
    try:
        validator = jsonschema.Draft7Validator(schema_data)
        validator.validate(json_data)
        print("JSON is valid against the schema.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        raise e

def load_json(file_paths):
    loaded_json_data = []
    print(file_paths)
    for file_path in file_paths:
        print(file_path)
        try:
            with open(file_path) as json_file:
                loaded_json_data.append(json.load(json_file))
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except json.JSONDecodeError:
            print(f"File {file_path} is not a valid JSON file")
    return loaded_json_data

def loads_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Load JSON data for each changed file
    json_data_list = load_json(changed_files)

    # Load JSON schema
    schema_file_path = 'schema.json'
    schema_data = loads_json(schema_file_path)

    # Validate each JSON against the schema
    for json_data in json_data_list:
        try:
            validate_json(json_data, schema_data)
        except jsonschema.exceptions.ValidationError as e:
            print("JSON is not valid against the schema.")
            print(e)
            sys.exit(1)  # Exit with failure status code

if __name__ == "__main__":
    main()
