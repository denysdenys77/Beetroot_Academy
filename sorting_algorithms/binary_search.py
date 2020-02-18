# реализовать работу бинарного поиска элемента

# my_list = range(1, 101)
#
#
# def binary_search(a_list, item):
#
#     first = 0
#     last = len(a_list) - 1
#
#     if len(a_list) == 0:
#         return f'{item} was not found in the list!'
#     else:
#         i = (first + last) // 2
#         if item == a_list[i]:
#             return f'{item} found'
#         else:
#             if a_list[i] < item:
#                 return binary_search(a_list[i+1:], item)
#             else:
#                 return binary_search(a_list[:i], item)
#
#
# print(binary_search(my_list, 69))

import sys

print(sys.executable)
