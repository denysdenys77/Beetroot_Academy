# Написать функцию-декоратор и класс таймер и декорировать им несколько функций с вычислениями.

import time


class Timer:

    def __init__(self, func):
        self.func = func
        self.time = 0

    def __call__(self, *args, **kwargs):
        start_t = time.time()
        self.func(*args, **kwargs)
        stop_t = time.time()
        print(start_t - stop_t)


@Timer
def print_hello():
    print('hello')

print_hello()



