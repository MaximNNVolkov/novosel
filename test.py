import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, insert, select
engine = db.create_engine('sqlite:///shows.db')
connection = engine.connect()

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200)),
)

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', String(200),  nullable=False),
    Column('user_id', Integer(), ForeignKey(users.c.id)),
)


metadata.create_all(engine)

ins = users.insert().values(
    id=160,
    name='Yatsenko'
)
connection.close()

print(ins.compile().params)
conn = engine.connect()
r = conn.execute(ins)

conn = engine.connect()
ins = insert(users)

r = conn.execute(ins, [{'id': 168, 'name': 'volkov'},
                       {'id': 169, 'name': 'vlasov'}])
# r = conn.execute(insert(users), users_list)
print(r.rowcount)
conn.close()

conn = engine.connect()
s = select([users]).where(users.columns.id > 140).where(users.columns.name == 'volkov')
r = conn.execute(s)
print(r.fetchall())
conn.close()
