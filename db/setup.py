from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///base.db'

engine = create_engine(DB_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = None

def initDB():
    Base.metadata.create_all(engine)
    
def save(instance):
    session = Session()
    session.add(instance)
    session.commit()
    # session.expunge_all()
    session.close()
    return instance
