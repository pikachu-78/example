import json
import jsonschema
import argparse
import sys

# Custom validation function for 'isNotEmpty'
def validate_is_not_empty(validator, isNotEmpty, instance, schema):
    if not isinstance(instance, str):
        return  # only validate strings
    if instance.strip() == "":
        yield jsonschema.ValidationError("Value must not be empty")

# Registering the custom keyword 'isNotEmpty'
jsonschema.Draft7Validator.VALIDATORS['isNotEmpty'] = validate_is_not_empty

def validate_json(json_data, schema_data):
    try:
        validator = jsonschema.Draft7Validator(schema_data)
        validator.validate(json_data)
        print(f"JSON in {json_data['file_path']} is valid against the schema.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON in {json_data['file_path']} is not valid against the schema.")
        print(e)
        return False

def load_json(file_paths):
    loaded_data = []
    for file_path in file_paths:
        try:
            with open(file_path) as json_file:
                json_data = json.load(json_file)
                json_data['file_path'] = file_path  # Store file path in json_data
                loaded_data.append(json_data)
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except json.JSONDecodeError:
            print(f"File {file_path} is not a valid JSON file")
    return loaded_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed_files", nargs='+', required=True)
    args = parser.parse_args()
    changed_files = args.changed_files
    
    print("Changed files:", changed_files)
    
    # Load JSON schema
    schema_file_path = 'schema.json'
    try:
        with open(schema_file_path, 'r') as schema_file:
            schema_data = json.load(schema_file)
    except FileNotFoundError:
        print(f"Schema file {schema_file_path} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Schema file {schema_file_path} is not a valid JSON file")
        sys.exit(1)

    # Load and validate each JSON file
    for json_data in load_json(changed_files):
        validate_json(json_data, schema_data)

if __name__ == "__main__":
    main()
