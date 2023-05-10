import json
from os import getcwd
from json_normalize import json_transformation

# Read in a JSON file
data_path = getcwd() + "/src/frameworks/requests/pandascore_streamlit_app/data"

with open(f"{data_path}/Dota 2_players_1_100.json", "r") as my_file:
    results = json.load(my_file)

print(json_transformation(results))