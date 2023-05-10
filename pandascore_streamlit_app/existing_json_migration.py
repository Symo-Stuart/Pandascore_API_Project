import json
import pandas as pd
from db_load import load_json_data
from db_connection import cursor
from os import getcwd, listdir
from sqlalchemy import text

# Connect to the database
cursor.connect()

# Path to the data
data_path = getcwd() + "/src/frameworks/requests/pandascore_streamlit_app/data"

# Retrieving All the JSON Files
json_files = [file for file in listdir(data_path)]

game_names, endpoint_names = zip(*[(elem.split("_")[0].lower(), elem.split("_")[1]) for elem in json_files])

print(game_names)
print(endpoint_names)

# DataFrame of Tables in Database
query = "select distinct table_name from INFORMATION_SCHEMA.columns where table_name not like 'pg%'"
tables = pd.read_sql_query(text(query), con=cursor)['table_name'].tolist()

print(tables)

for i, game in enumerate(game_names):
    endpoint_name = endpoint_names[i]
    json_file = json_files[i]

    with open(f"{data_path}/{json_file}", "r") as my_file:
        json_data = json.load(my_file)

    load_json_data(game, endpoint_name, json_data, cursor)

    print(f"Table {game}_{endpoint_name} has more data added.")
