from setup import engine, Base
from models import Article


def init():
    Base.metadata.create_all(engine)

init()

article = Article(
    code='amono',
    designation='Designation'
)