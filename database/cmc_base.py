import app_logger as loger
from .db_start import db_conn, Users, UserSales
import time


log = loger.get_logger(__name__)
date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
date = time.strftime('%Y-%m-%d', time.localtime())


def add_user(user):
    log.info(
        'Запрос на добавление нового пользователя с '
        '{}, {}, {}, {}.'.format(user.id, user.first_name, user.last_name, user.username))
    u = Users(user_id=user.id,
              first_name=user.first_name,
              last_name=user.last_name,
              user_name=user.username)
    conn = db_conn()
    conn.add(u)
    conn.commit()


def user_check(user):
    log.info('Запрос на поиск пользователя {}.'.format(user.id))
    conn = db_conn()
    s = conn.query(Users.user_id).filter(Users.user_id == user.id).all()
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def save_res(u_id: int, res: dict):
    log.info(
        'Запрос на сохранение записи {}, {}.'.format(u_id, res))
    u = UserSales(
        user_id=res.get('id'),
        date=date,
        bch=res.get('bch'),
        sup=res.get('sup'),
        szdor=res.get('szdor')
    )
    conn = db_conn()
    conn.add(u)
    conn.commit()


def sales_check(u_id: int, res: dict):
    log.info('Запрос на поиск продаж пользователя {} за дату {}.'.format(u_id, date))
    conn = db_conn()
    s = conn.query(UserSales.id).filter(UserSales.user_id == res.get('id'), UserSales.date == date)
    log.info(s.count())
    if s.count() > 0:
        res = 'alredy_send'
        log.info('alredy_send')
    else:
        res = 'ok_sale'
    return res
