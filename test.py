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


c = config
p = c.get('atrs', 'properties')
d = p.split(',')
my_d ={}
for i in d:
    k,v = i.split(':')
    my_d.update({k:v})
print(my_d.values())
print(my_d.keys())
b = [4563]
for v in my_d.values():
    b.append(v)
print(b)
print(86101//10)