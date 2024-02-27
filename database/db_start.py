from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DATABASE = {
    'drivername': 'sqlite',
    'database': 'shows.db'
}


engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()


class Users(DeclarativeBase):
    __tablename__ = 'users'

    user_id = Column('user_id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    user_name = Column('user_name', String)

    def __repr__(self):
        return f"<user_id={self.user_id}," \
               f"first_name={self.first_name}," \
               f"last_name={self.last_name}," \
               f"user_name={self.user_name}>"

    @property
    def serialize(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name
        }


class Answers(DeclarativeBase):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    date = Column(DateTime(), default=datetime.now)
    otv_1 = Column(String)
    otv_2 = Column(String)
    otv_3 = Column(String)
    otv_4 = Column(String)
    otv_5 = Column(String)


def db_conn():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
