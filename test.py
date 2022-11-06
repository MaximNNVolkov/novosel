
class UserSales:
    """хранение атрибутов продаж"""
    available_properities = ['id', 'bch', 'sup', 'sprime']

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


u = UserSales()
u.set('id', 345678)
u.set('bch', 5)
u.set('sup', 6)
u.set('sprime', 0)
u.pr()
print(u.__dict__.keys()[0])
print(u.available_properities)
print(u.__dict__.keys()==u.available_properities)
