
from db.setup import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    code = Column('code', String(10))
    designation = Column('designation', String(100))
    family = Column('family', String(50))
    author = Column('author', String(50))
    editor = Column('editor', String(50))
    buying_price = Column('buying_price', String(20))
    selling_price = Column('selling_price', String(20))
    quantity = Column('quantity', Integer)
    command_entry = relationship(
        'CommandEntry', back_populates='article')
    # selling_entry = relationship(
    #     'SellingEntry', uselist=False, back_populates='parent')

class Provider(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True)
    full_name = Column('full_name', String(50))
    commands = relationship('Command')


class Command(Base):
    __tablename__ = 'command'
    id = Column(Integer, primary_key=True)
    emission_date = Column('emission_date', Date)
    reception_date = Column('reception_date', Date)
    motif = Column('motif', String(250))
    receptionned = Column('receptionned', Boolean, default=False)
    # receptionner = Column('receptionner', String(30))
    command_entries = relationship('CommandEntry')
    provider_id = Column(Integer, ForeignKey('provider.id'))
    provider = relationship('Provider', back_populates='commands')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.receptionned = False

class CommandEntry(Base):
    __tablename__ = 'command_entry'
    id = Column(Integer, primary_key=True)
    cmd_qte = Column('commanded_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', back_populates='command_entry')
    command_id = Column(Integer, ForeignKey('command.id'))


class Selling(Base):
    __tablename__ = 'selling'
    id = Column(Integer, primary_key=True)
    selling_date = Column('selling_date', Date)
    selling_type = Column('selling_type', String(30))
    total_selling = Column('total_selling', Integer)
    selling_entries = relationship('SellingEntry')


class SellingEntry(Base):
    __tablename__ = 'selling_entry'
    id = Column(Integer, primary_key=True)
    selling_qte = Column('selling_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', uselist=False)
    selling_id = Column(Integer, ForeignKey('selling.id'))
