# Объявить класс Person с переменной класса _secret_data и переменной инстанса is_admin. Написать декоратор, который
# проверяет есть ли у пользователя доступ к данной функции(if is_admin). Применить декоратор к методу класса
# Person.get_secret_data (getter для _secret_data). Создать несколько объектов Person с разными is_admin значениями и
# вызвать у каждого метод get_secret_data.


def access(f):
    def wrapper(self):
        if self.is_admin == 'admin':
            x = Person._secret_data
            return x
        else:
            return 'no access'
    return wrapper


class Person:
    _secret_data = 'my secret data'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    @access
    def get_secret_data(self):
        return Person._secret_data


petya = Person('admin')
vasya = Person('user')


p = petya.get_secret_data()
v = vasya.get_secret_data()

print(p)
print(v)

