import pandas as pd
from sqlalchemy.types import JSON, TEXT

# Helper Function
def load_json_data(game_name: str, endpoint_name: str, json_data: list, cursor):
    # Connect to DB
    cursor.connect()
    
    # Convert the Data into a Dictionary
    json_dict = {'data' : json_data}

    # Convert into pandas DataFrame
    df = pd.DataFrame.from_dict(json_dict)

    # Add Additional Columns
    df['game'] = game_name
    df['endpoint'] = endpoint_name

    # Column Reordering
    df = df[['game', 'endpoint', 'data']]

    # Load to PostgreSQL
    df.to_sql(f'{game_name.lower()}_{endpoint_name}', con=cursor, dtype={'game': TEXT, 'endpoint': TEXT, 'data': JSON}, if_exists='append', index=False)

    return df


