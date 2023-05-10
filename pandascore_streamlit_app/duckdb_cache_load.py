import pandas as pd
from duckdb_con import cursor
from app import game_options, game_short_forms, endpoint_options

# Get the Game Options and Endpoint Names
game_df = pd.DataFrame.from_dict({'name': game_options, 'short_name': game_short_forms})
endpoint_df = pd.DataFrame.from_dict({'endpoint': endpoint_options})

# Load Above Tables into DuckDB
game_df.to_sql('games', con=cursor, index=False, if_exists='replace')
endpoint_df.to_sql('endpoints', con=cursor, index=False, if_exists='replace')

print("Games and Endpoints tables loaded into duckDB successfully!")