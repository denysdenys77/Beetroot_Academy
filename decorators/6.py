# Объявить глобальную переменную history (пустой список) и реализовать функцию-декоратор, которая при вызове функции
# будет добавлять информацию о ней в history. Задекорировать несколько функций и вызвать их. В конце вывести
# history на экран.
from functools import reduce


history = []


def history_append(f):
    def wrapper(*args):
        global history
        history.append(f)
    return wrapper

@history_append
def the_sum(x, y):
    return x + y

@history_append
def perimeter(*args):
    return reduce(lambda x, y: x + y, args)

a = the_sum(3, 7)
b = perimeter(3, 7, 4, 8, 9)

print(history)