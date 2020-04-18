
from setup import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    code = Column('code', String(10))
    designation = Column('designation', String(100))
    family = Column('family', String(50))
    author = Column('author', String(50))
    buying_price = Column('buying_price', String(20))
    selling_price = Column('selling_price', String(20))
    quantity = Column('quantity', Integer)
    # command_entry = relationship(
    #     'CommandEntry', uselist=False, back_populates='parent')
    # selling_entry = relationship(
    #     'SellingEntry', uselist=False, back_populates='parent')


class Provider(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True)
    full_name = Column('full_name', String(50))
    phone_number = Column('phone_number', String(20))
    # command = relationship('Command')


class Command(Base):
    __tablename__ = 'command'
    id = Column(Integer, primary_key=True)
    cmt_date = Column('cmd_date', Date)
    object_ = Column('object', String(50))
    receptionner = Column('receptionner', String(30))
    command_entry = relationship('CommandEntry')
    provider = Column(Integer, ForeignKey('provider.id'))


class CommandEntry(Base):
    __tablename__ = 'command_entry'
    id = Column(Integer, primary_key=True)
    cmd_qte = Column('commanded_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', uselist=False)
    command_id = Column(Integer, ForeignKey('command.id'))


class Selling(Base):
    __tablename__ = 'selling'
    id = Column(Integer, primary_key=True)
    selling_date = Column('selling_date', Date)
    selling_type = Column('selling_type', String(30))
    total_selling = Column('total_selling', Integer)
    # selling_entries = relationship('SellingEntry')


class SellingEntry(Base):
    __tablename__ = 'selling_entry'
    id = Column(Integer, primary_key=True)
    selling_qte = Column('selling_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', uselist=False)
    selling_id = Column(Integer, ForeignKey('selling.id'))
