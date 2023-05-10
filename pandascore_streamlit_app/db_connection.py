from sqlalchemy import create_engine

username = 'stuartb'
password = 'stuart2023!'
server = '104.225.217.176'
port = 8200
database = 'esports'

dialect = f'postgresql://{username}:{password}@{server}:{port}/{database}'

cursor = create_engine(dialect)
