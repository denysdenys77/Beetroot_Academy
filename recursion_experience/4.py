# Написать рекурсивную функцию для подсчета возведения числа в степень.


def exponentiation(num, power):
    if power == 1:
        return num
    else:
        return exponentiation(num, power - 1) * num

print(exponentiation(4, 4))
