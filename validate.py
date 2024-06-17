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
        print("JSON is valid against the schema.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        raise e 

def load_json(file_path):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except json.JSONDecodeError:
        print(f"File {file_path} is not a valid JSON file")
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed_files", nargs='+', help="List of changed JSON files")
    args = parser.parse_args()

    changed_files = args.changed_files

    if not changed_files:
        print("No files provided.")
        sys.exit(1)

    for file_path in changed_files:
        print(f"Validating file: {file_path}")
        json_data = load_json(file_path)

        if json_data is not None:
            # Load JSON schema
            schema_file_path = 'schema.json'
            schema_data = load_json(schema_file_path)

            if schema_data is not None:
                # Validate JSON against the schema
                try:
                    validate_json(json_data, schema_data)
                except jsonschema.exceptions.ValidationError as e:
                    print(f"JSON in file {file_path} is not valid against the schema.")
                    print(e)
                    sys.exit(1)  # Exit with failure status code

if __name__ == "__main__":
    main()
