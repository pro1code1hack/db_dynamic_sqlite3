from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from dotenv import load_dotenv
import os


load_dotenv()


class DB:

    def __init__(self) -> None:
        self.db_url = self.build_url()
        self.engine = create_engine(self.db_url)        
        self.session = self.get_session()


    # postgresql://yehorq1w2e3@localhost/py5
    def build_url(self):
        return f'postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}/{os.environ["POSTGRES_DB"]}'

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

db = DB()

Base = declarative_base()