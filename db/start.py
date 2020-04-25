'''This file is for testing'''

from setup import engine, Base
from models import Article

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


article = Article(
    code='amono',
    designation='Designation'
)

session = Session()

session.add(article)
session.commit()
session.close()