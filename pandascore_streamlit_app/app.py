import requests
import json
import pandas as pd
import streamlit as st
from os import getcwd, listdir
from json_normalize import json_transformation
from db_connection import cursor
from db_load import load_json_data
from duckdb_con import cursor

# Create a title
st.title("Pandascore API Data Retrieval")

# Encrypted Text Input
api_token = st.text_input("Paste in your Pandascore API Token: ", type='password')

# # Customization Text Inputs
# game_options = ['Counter Strike: Global Offensive', 'Call of Duty: Modern Warfare', 'Dota 2', 'FIFA', 'League of Legends', 'Overwatch', 'Public Underground Battle Ground (PUBG)', 'Rainbow Six Siege', 'Rocket League', 'Valorant', 'King of Glory', 'League of Legends: Wild Rift', 'Starcraft 2', 'Starcraft: Brood War']
# game_short_forms = ['csgo', 'codmw', 'dota2', 'fifa', 'lol', 'ow', 'pubg', 'r6siege', 'rl', 'valorant', 'kog', 'lol-wild-rift', 'starcraft-2', 'starcraft-brood-war']
game_df = pd.read_sql('games', con=cursor)

game_options = game_df['name'].tolist()
game_short_forms = game_df['short_name'].tolist()
game_api_map = {game: game_short_forms[i] for i, game in enumerate(game_options)}

game_name = st.selectbox("Choose a game: ", options=game_options)

endpoint_df = pd.read_sql('endpoints', con=cursor)
endpoint_options = endpoint_df['endpoint'].tolist()
# endpoint_options = ['leagues', 'matches', 'players', 'series', 'teams', 'tournaments']
endpoint_name = st.selectbox("Choose an endpoint: ", options=endpoint_options)

st.markdown("---")
st.markdown("<h3 style='text-align:center'> Query Parameters </h3>", unsafe_allow_html=True)

# Query Parameters
page_number = st.number_input("Choose a page number: ", min_value=1, max_value=10, value=1)
per_page = st.number_input("Choose number of entries per page: ", min_value=10, max_value=100, step=10)

# Create the Logic
data_path = getcwd() + "/data"

# Get JSON File Name
json_file_name = f"{game_name}_{endpoint_name}_{page_number}_{per_page}.json"

# Customized URL
url = f"https://api.pandascore.co/{game_api_map[game_name]}/{endpoint_name}?sort=&page={page_number}&per_page={per_page}&token={api_token}"

# Function to execute API call
def api_call(url):
    
    # Retrieve a response
    response = requests.get(url)
    
    # JSON Data Variable
    json_data = response.json()

    # Create context manager
    with open(f"{data_path}/{json_file_name}", "w") as my_file:
        json.dump(json_data, my_file)
    
    # Save to database
    load_json_data(game_name.lower(), endpoint_name, json_data, cursor)

    return url

# Create the button
if st.button("Retrieve Data"):
    if json_file_name in listdir(data_path):
        st.info(f"Your data is already saved in {json_file_name}")
    else:
        api_call(url)
        st.success(f"URL {url} data received successfully.")

# Create button for viewing the transformation
if st.button("View Transformation"):
    # Create context manager
    with open(f"{data_path}/{json_file_name}", "r") as my_file:
        result = json.load(my_file)

    result_df = json_transformation(result)

    st.dataframe(result_df)

    
