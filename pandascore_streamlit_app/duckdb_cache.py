import duckdb
from os import getcwd

# Data Path
data_path = getcwd() + "/src/frameworks/requests/pandascore_streamlit_app/data"

# Create a new database called pandascore_cache
connector = duckdb.connect(f"{data_path}/pandascore_cache.duckdb")

# Set up the cursor
c = connector.cursor()

# Execute simple query
c.sql("select 'hi'")
