import json

def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config

print(load_json("car_config.json"))
print("print(upper(vertical))".upper())