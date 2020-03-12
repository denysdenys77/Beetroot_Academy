# Написать функцию-декоратор, которая будет выводить на экран с какими аргументами вызывается функция.

def show_arguments(f):
    def wrapper(*args):
        l = [str(x) for x in args]
        str_args = ', '.join(l)
        print(f'Function was called with: {str_args}')
    return wrapper


@show_arguments
def the_sum(x, y):
    return x + y


a = the_sum(3, 7)
