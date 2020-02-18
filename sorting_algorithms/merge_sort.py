# реализовать работу сортировки слиянием.

my_list = [3, 7, 1, 2, 5, 9, 6, 4, 8]


def merge_sort(n):
    if len(n) > 1:
        mid = len(n) // 2  # находим делитель
        left = n[:mid]
        right = n[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # перезаписываем значения элементов входящего списка
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[k] = left[i]
                i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1

        # проверка на оставшиеся элементы
        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1


merge_sort(my_list)
print(my_list)
