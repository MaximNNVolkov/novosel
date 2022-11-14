import app_logger as loger
from .db_start import Users, cr_users
import time


log = loger.get_logger(__name__)
db_name = 'cmc.db'
date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
date = time.strftime('%Y-%m-%d', time.localtime())


def add_user(user):
    log.debug(
        'Запрос на добавление нового пользователя с '
        '{}, {}, {}, {}.'.format(user.id, user.first_name, user.last_name, user.username))
    u = cr_users()
    u.insert().values(id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)


def user_check(user):
    log.debug('Запрос на поиск пользователя {}.'.format(user.id))
    u = cr_users()
    s = u.select(id == user.id)
    print(s)
    all_results = False
    if all_results:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def save_res(u_id: int, res: dict):
    log.debug(
        'Запрос на сохранение записи {}, {}.'.format(u_id, res))
    conn, cur = con_up()
    m = [u_id, date, int(res['id'])//10]
    for v in res.values():
        m.append(v)
    cur.execute('INSERT INTO sales_fact VALUES (?, ?, ?, ?, ?, ?, ?)', m)
    con_close(conn)
