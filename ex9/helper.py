import json

def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config
#
# //{
# //	"O":[2,[0,3],0],
# //	"R":[2,[0,0],1],
# //	"W":[4,[3,2],1]
# //}