from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import MetaData, UniqueConstraint

engine = create_engine('sqlite:///news.db', echo=True)


meta = MetaData()



News = Table(
    'news', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('content', String),
    Column('category', String),
    UniqueConstraint('title', name='title')
)

meta.create_all(engine)
