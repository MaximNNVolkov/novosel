import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, insert, select


def cr_users():
    metadata = MetaData()
    engine = db.create_engine('sqlite:///shows.db')
    connection = engine.connect()
    users = Users(metadata)
    metadata.create_all(engine)
    connection.close()
    return users.users


class Users():

    def __init__(self, metadata):
        users = Table('users', metadata,
            Column('id', Integer(), primary_key=True),
            Column('first_name', String(200)),
            Column('last_name', String(200)),
            Column('username', String(200)),
        )
        self.users = users


def create_sales():
    metadata = MetaData()
    posts = Table('posts', metadata,
        Column('id', Integer(), primary_key=True),
        Column('post_title', String(200), nullable=False),
        Column('post_slug', String(200),  nullable=False),
        Column('content', String(200),  nullable=False),
        Column('user_id', Integer(), ForeignKey(users.c.id)),
    )
    return posts
