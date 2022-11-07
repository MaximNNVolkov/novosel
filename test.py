import configparser
from aiogram.dispatcher.filters.state import State, StatesGroup


config = configparser.ConfigParser()
config.read("config.ini")


class UserSales:
    """хранение атрибутов продаж"""
    available_properities = config['atrs']['properties']

    def pr(self):
        for a in self.__dict__:
            print(a, self.__getattribute__(a))

    def set(self, name: str, value: int):
        """список атрибутов"""
        if name in self.available_properities:
            self.__setattr__(name, value)
        else:
            raise ValueError('Недопустимый атрибут')

    def check(self):
        return True


class StateUser(StatesGroup):

    def __init__(self, states):
        for i in states:
            print(i)
            i = State()


u = UserSales()
u.set('id', 345678)
u.set('bch', 5)
u.set('sup', 6)
u.set('szdor', 0)
u.pr()
u = UserSales()
u.set('id', 22222)
u.pr()