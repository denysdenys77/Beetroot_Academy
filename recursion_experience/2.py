# Определить будет ли строка палиндромом используя рекурсию.

my_str = '1234554321'


def is_palindrome(my_str):
    if not my_str or len(my_str) == 1:
        return True
    elif my_str[0] != my_str[-1]:
        return False
    else:
        return is_palindrome(my_str[1:-1])


print(is_palindrome(my_str))
