from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'sqlite:///base.db'

engine = create_engine(DB_URL)

Base = declarative_base()
