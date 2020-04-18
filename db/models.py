
from db.setup import BaseModel
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class Article(BaseModel):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    code = Column('code', String(10))
    designation = Column('designation', String(100))
    family = Column('family', String(50))
    author = Column('author', String(50))
    buying_price = Column('buying_price', String(20))
    selling_price = Column('selling_price', String(20))
    quantity = Column('quantity', Integer)
    command_entry = relationship(
        'CommandEntry', uselist=False, back_populates='parent')
    selling_entry = relationship(
        'SellingEntry', uselist=False, back_populates='parent')


class Provider(BaseModel):
    __tablename__ = 'provider'
    full_name = Column('full_name', String(50))
    phone_number = Column('phone_number', String(20))
    command = relationship('Command')


class Command(BaseModel):
    __tablename__ = 'command'
    id = Column(Integer, primary_key=True)
    cmt_date = Column('cmd_date', Date)
    object_ = Column('object', String(50))
    receptionner = Column('receptionner', String(30))
    command_entry = relationship('CommandEntry')
    provider = Column(Integer, ForeignKey('provider.id'))


class CommandEntry(BaseModel):
    __tablename__ = 'command_entry'
    id = Column(Integer, primary_key=True)
    cmd_qte = Column('commanded_qte', Integer)
    article = relationship('Article', back_populates='child')
    command_id = Column(Integer, ForeignKey('command.id'))


class Selling(BaseModel):
    __tablename__ = 'selling'
    selling_date = Column('selling_date', Date)
    selling_type = Column('selling_type', String(30))
    total_selling = Column('total_selling', Integer)
    selling_entries = relationship('SellingEntry')


class SellingEntry(BaseModel):
    __tablename__ = 'selling_entry'
    id = Column(Integer, primary_key=True)
    selling_qte = Column('selling_qte', Integer)
    article = relationship('Article', back_populates='child')
    selling_id = Column(Integer, ForeignKey('selling.id'))
