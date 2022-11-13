import app_logger as loger
import sqlite3
import time


log = loger.get_logger(__name__)
db_name = 'cmc.db'
date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
date = time.strftime('%Y-%m-%d', time.localtime())


def con_up():
    log.debug('Установка соединения с {}.'.format(db_name))
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur


def con_close(conn):
    log.debug('Закрытие соединения с {}.'.format(db_name))
    conn.commit
    conn.close()


def add_user(user):
    log.debug(
        'Запрос на добавление нового пользователя с '
        '{}, {}, {}, {}.'.format(user.id, user.first_name, user.last_name, user.username))
    conn, cur = con_up()
    m = [user.id, user.first_name, user.last_name, user.username]
    cur.execute('INSERT INTO users VALUES (?, ?, ?, ?)', m)
    con_close(conn)


def user_check(user):
    log.debug('Запрос на поиск пользователя {}.'.format(user.id))
    conn, cur = con_up()
    cur.execute("SELECT user_id FROM users WHERE user_id = ?;", [user.id])
    all_results = cur.fetchall()
    if all_results:
        res = 'ok_user'
    else:
        res = 'no_user'
    con_close(conn)
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
