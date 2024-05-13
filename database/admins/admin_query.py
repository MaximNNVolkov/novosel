import app_logger as loger
from database.db_start import db_conn, Admins, Users, Answers, Photos


log = loger.get_logger(__name__)


def admins_list():
    log.info(f'Запрос на список администраторов')
    conn = db_conn()
    s = conn.query(Admins.user_id).all()
    if len(s) > 0:
        res = s
    else:
        res = ()
    return res


def get_users_list(between: list = ['1990-01-01', '2990-01-01']):
    log.info(f'Запрос на получение списка пользователей')
    conn = db_conn()
    s = conn.query(Users.user_id)\
        .filter((Users.date >= between[0]) & (Users.date <= between[1])).all()
    if len(s) > 0:
        res = s
    else:
        res = ()
    return res


def get_answers_list(between: list = ['1990-01-01', '2990-01-01']):
    log.info(f'Запрос на получение списка ответов')
    conn = db_conn()
    s = conn.query(Answers.id)\
        .filter((Answers.date >= between[0]) & (Answers.date <= between[1])).all()
    if len(s) > 0:
        res = s
    else:
        res = ()
    return res


def add_photo_query(file_id: str, id_who_add: int, name: str):
    log.info(f'Запрос на добавление фото {file_id}, от {id_who_add}.')
    p = Photos(
        file_id=file_id,
        who_add=id_who_add,
        photo_name=name
    )
    conn = db_conn()
    conn.add(p)
    conn.commit()
