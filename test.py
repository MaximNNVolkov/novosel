from database.db_start import db_conn, Users


session = db_conn()
new_user = Users(
    user_id=124,
    first_name='fn',
    last_name='ln',
    user_name='un'
)

#session.add(new_user)
#session.commit()
post = session.query(Users).filter(Users.user_id == 123)
print(post.count())
for p in post:
    print(p.user_id)
print(new_user.user_id)
