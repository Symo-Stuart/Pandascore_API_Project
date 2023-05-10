from sqlalchemy import create_engine
from os import getcwd

# Creating the data path
data_path = getcwd() + "/data"

# Dialect
dialect = f'sqlite:////{data_path}/pandascore_cache.db'

engine = create_engine(dialect)