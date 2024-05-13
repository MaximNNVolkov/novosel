from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import app_logger as loger


log = loger.get_logger(__name__)


DATABASE = {
    'drivername': 'sqlite',
    'database': 'shows.db'
}


engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()


class Users(DeclarativeBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    date = Column(DateTime(), default=datetime.now)
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


class Admins(DeclarativeBase):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    date = Column(DateTime(), default=datetime.now)
    who_add = Column(Integer)


class Photos(DeclarativeBase):
    __tablename__ = 'photos'

    file_id = Column(String, primary_key=True)
    who_add = Column(Integer)
    date = Column(DateTime(), default=datetime.now)
    photo_name = Column(String)


def db_conn():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def write_main_admin_db(u_id: int):
    log.info(f'Добавление главного админа {u_id}, от .')
    conn = db_conn()
    s = conn.query(Admins.user_id).filter(Admins.user_id == u_id).all()
    if len(s) > 0:
        log.info('main_admin_already_added')
    else:
        u = Admins(
            user_id=u_id,
            who_add=u_id,
        )
        conn = db_conn()
        conn.add(u)
        conn.commit()
        log.info('main_admin_added')
