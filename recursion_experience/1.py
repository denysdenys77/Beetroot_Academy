# Найти сумму всех чисел в списке используя рекурсию.

my_list = [1, 2, 3, 4, 5, 6]


def sum_of_my_list(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return sum_of_my_list(my_list[:-1]) + my_list[-1]


print(sum_of_my_list(my_list))
