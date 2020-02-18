# реализовать работу быстрой сортировки

my_list = [3, 7, 1, 2, 5, 9, 6, 4, 8]


def quick_sort(n):
    if len(n) == 1:
        return n
    else:
        base = n[-1]
        less = []
        more = []
        for elem in n[:-1]:
            if elem < base:
                less.append(elem)
            else:
                more.append(elem)

        return quick_sort(less) + [base] + quick_sort(more)


print(quick_sort(my_list))
