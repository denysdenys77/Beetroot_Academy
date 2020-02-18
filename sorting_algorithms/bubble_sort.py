# реализовать работу сортировки пузырьком.

import random

my_list = random.sample(range(1, 50), 10)
print(my_list)


i = 1
while i != len(my_list):
    cur = 0
    next = 1

    j = 1
    while j != len(my_list):
        if my_list[cur] < my_list[next]:
            cur += 1
            next += 1
        elif my_list[cur] > my_list[next]:
            cur_item = my_list[cur]
            next_item = my_list[next]

            my_list[cur] = next_item
            my_list[next] = cur_item

            cur += 1
            next += 1

        j += 1

    i += 1

print(my_list)
