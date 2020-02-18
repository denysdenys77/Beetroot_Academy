# Написать декоратор, который будет валидировать входные данные (параметры декорируемой функции, например разрешить
# только числа). Применить декоратор к функции, которая принимает несколько чисел.


def validate(func):
    def wrapper(*args):
        a = sorted(args)
        return a
    return wrapper


@validate
def the_sum(*args):
    return args


x = the_sum(5, 1, 6, 2, 4, 7)
print(x)
