from sqlalchemy import create_engine

engine = create_engine('sqlite:///news.db', echo=True)


from sqlalchemy import MetaData
meta = MetaData()

from sqlalchemy import Table, Column, Integer, String, MetaData


News = Table(
    'news', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('content', String),
    Column('category', String)
)

# meta.create_all(engine)
