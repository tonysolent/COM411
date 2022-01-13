import json
def read(file):
    with open(file) as my_file:
        info = json.load(my_file)
        city = info["city"]
