import os


database = os.getenv('DATABASE')
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')
database_password = os.getenv('DATABASE_PASSWORD')
database_user = os.getenv('DATABASE_USER')

# database_uri = f'postgresql+asyncpg://{database_user}:{database_password}@{database_host}:{database_port}/{database}'
async_database_uri = 'postgresql+asyncpg://postgres:postgres@localhost:5430/postgres'
sync_database_uri = 'postgresql+psycopg2://postgres:postgres@localhost:5430/postgres'


class DatabaseURI:
    def __init__(self):
        self.database_uri = sync_database_uri
        self.connection_type = 'sync'

    def turn_async(self):
        self.database_uri = async_database_uri
        self.connection_type = 'async'
        print('Im async')

db_uri = DatabaseURI()