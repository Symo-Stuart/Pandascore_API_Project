import pandas as pd
from sqlite_cache_connection import engine
from sqlalchemy import text

cursor = engine.connect()

info = text("select name, type from sqlite_schema")

df = pd.read_sql_query(info, con=cursor)

print(df)

# game_df = pd.read_sql_table('game_options', con=cursor)
# endpoint_df = pd.read_sql_table('endpoint_options', con=cursor)
