from sqlalchemy import Table, Column, Integer, MetaData, String

metadata = MetaData()

worker_table = Table(
    'worker',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)
