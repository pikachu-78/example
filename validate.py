import json
import jsonschema

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
        print("JSON is not valid against the schema.")
        print(e)
        return False

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Load JSON data
    json_file_path = 'copy.json'
    json_data = load_json(json_file_path)

    # Load JSON schema
    schema_file_path = 'schema.json'
    schema_data = load_json(schema_file_path)

    # Validate JSON against the schema
    validate_json(json_data, schema_data)

if __name__ == "__main__":
    main()
