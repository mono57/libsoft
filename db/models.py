
from db.setup import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
import datetime


# Abstract Class
# class TimeStampModel(Base):
#     __tablename__ = 'timestampmodel'
#     id = Column(Integer, primary_key=True)
#     created_at = Column('created_at', Date)
#     updated_at = Column('updated_at', Date)
#     type_ = Column(String(50))

#     __mapper_args__ = {
#         'polymorphic_identity':'timestampmodel',
#         'polymorphic_on': type_
#     }

#     def __init__(self, *args, **kwargs):
#         super(TimeStampModel, self).__init__(*args, **kwargs)
#         today = datetime.date.today()
#         self.created_at = today
#         self.updated_at = today

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
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)
    archived = Column('archived', Boolean)
    command_entry = relationship(
        'CommandEntry', back_populates='article')
    selling_entry = relationship(
        'SellingEntry', back_populates='article')

    # __mapper_args__ = {
    #     'polymorphic_identity':'article',
    # }
    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        self.archived = False
        self.created_at = today
        self.updated_at = today

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    full_name = Column('full_name', String(50))
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)
    # sellings = relationship('Selling')

    # __mapper_args__ = {
    #     'polymorphic_identity':'provider',
    # }
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today

class Provider(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True)
    full_name = Column('full_name', String(50))
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)
    commands = relationship('Command')

    # __mapper_args__ = {
    #     'polymorphic_identity':'provider',
    # }
    def __init__(self, *args, **kwargs):
        super(Provider, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today
class Command(Base):
    __tablename__ = 'command'
    id = Column(Integer, primary_key=True)
    emission_date = Column('emission_date', Date)
    reception_date = Column('reception_date', Date)
    motif = Column('motif', String(250))
    receptionned = Column('receptionned', Boolean)
    archived = Column('archived', Boolean)
    date_reception = Column('receptionned_date', Date)
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)
    # receptionner = Column('receptionner', String(30))
    date_cmd = Column('date', Date)
    command_entries = relationship('CommandEntry')
    provider_id = Column(Integer, ForeignKey('provider.id'))
    provider = relationship('Provider', back_populates='commands')

    # __mapper_args__ = {
    #     'polymorphic_identity':'command',
    # }

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.receptionned = False
        self.archived = False
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today

class CommandEntry(Base):
    __tablename__ = 'command_entry'
    id = Column(Integer, primary_key=True)
    cmd_qte = Column('commanded_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', back_populates='command_entry')
    command_id = Column(Integer, ForeignKey('command.id'))
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)

    # __mapper_args__ = {
    #     'polymorphic_identity':'command_entry',
    # }
    def __init__(self, *args, **kwargs):
        super(CommandEntry, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today

class Selling(Base):
    __tablename__ = 'selling'
    id = Column(Integer, primary_key=True)
    selling_date = Column('selling_date', Date)
    selling_type = Column('selling_type', String(30))
    total_selling = Column('total_selling', Integer)
    client = Column('client', String(50))
    archived = Column('archived', Boolean)
    selling_entries = relationship('SellingEntry')
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)
    # client_id = Column(Integer, ForeignKey('client.id'))
    # client = relationship('Client', back_populates='sellings')

    # __mapper_args__ = {
    #     'polymorphic_identity':'selling',
    # }

    def __init__(self, *args, **kwargs):
        super(Selling, self).__init__(*args, **kwargs)
        self.archived = False
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today

class SellingEntry(Base):
    __tablename__ = 'selling_entry'
    id = Column(Integer, primary_key=True)
    selling_qte = Column('selling_qte', Integer)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship('Article', back_populates='selling_entry')
    selling_id = Column(Integer, ForeignKey('selling.id'))
    created_at = Column('created_at', Date)
    updated_at = Column('updated_at', Date)

    # __mapper_args__ = {
    #     'polymorphic_identity':'selling_entry',
    # }
    def __init__(self, *args, **kwargs):
        super(SellingEntry, self).__init__(*args, **kwargs)
        today = datetime.date.today()
        self.created_at = today
        self.updated_at = today
