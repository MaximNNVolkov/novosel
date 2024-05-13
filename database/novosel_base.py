import app_logger as loger
from .db_start import db_conn, Users, Answers, Admins, Photos
import time


log = loger.get_logger(__name__)
date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
date = time.strftime('%Y-%m-%d', time.localtime())


def add_user(user):
    log.info(
        f'Запрос на добавление нового пользователя с '
        f'{user.id}, {user.first_name}, {user.last_name}, {user.username}.')

    u = Users(user_id=user.id,
              first_name=user.first_name,
              last_name=user.last_name,
              user_name=user.username)
    conn = db_conn()
    conn.add(u)
    conn.commit()


def user_check(user):
    log.info(f'Запрос на поиск пользователя {user.id}.')
    conn = db_conn()
    s = conn.query(Users.user_id).filter(Users.user_id == user.id).all()
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def save_res(u_id: int, res: list):
    log.info(f'Запрос на сохранение записи {u_id}, {res}.')
    otv = []
    for i in res:
        otv.append([v for v in i.values()][0])
    u = Answers(
        user_id=u_id,
        otv_1=otv[0],
        otv_2=otv[1],
        otv_3=otv[2],
        otv_4=otv[3],
        otv_5=otv[4],
    )
    conn = db_conn()
    conn.add(u)
    conn.commit()


def admin_check(new_admin_id: int):
    log.info(f'Запрос на поиск админа {new_admin_id}.')
    conn = db_conn()
    s = conn.query(Admins.user_id).filter(Admins.user_id == new_admin_id).all()
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def write_admin_db(u_id: int, id_who_add: int):
    log.info(f'Добавление нового админа {u_id}, от {id_who_add}.')
    if admin_check(u_id) == 'ok_user':
        return 'user_already_added'
    else:
        u = Admins(
            user_id=u_id,
            who_add=id_who_add,
        )
        conn = db_conn()
        conn.add(u)
        conn.commit()
        return 'admin_added'


def get_photo(photo_name: str):
    log.info(f'Запрос на получение фото {photo_name}.')
    conn = db_conn()
    s = conn.query(Photos).filter(Photos.photo_name == photo_name).all()
    if len(s) > 0:
        res = s[0].file_id
    else:
        res = 'no_photo'
    return res
