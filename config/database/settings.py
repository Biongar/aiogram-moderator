from databases import Database
from sqlalchemy.ext.declarative import declarative_base


from config.settings import DATABASE_SETTINGS as db

DATABASE_URL = f"postgresql://{db['USER']}:{db['PASSWORD']}@{db['HOST']}/{db['NAME']}"

database = Database(DATABASE_URL)
Base = declarative_base()