from sqlalchemy import create_engine
from os import getcwd

# Setup DuckDB Connection
data_path = getcwd() + "/data"
dialect = f'duckdb:////{data_path}/pandascore_cache.duckdb'

# Set up the engine and cursor
engine = create_engine(dialect)
cursor = engine.connect()