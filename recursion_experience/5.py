# реализовать функцию рекурсивного обхода файлов, которая будет выводить информацию о содержимом папки и вложенных
# папок. Если в папке есть вложенная папка ее тоже нужно обойти и вывести ее содержимое.

import os


def os_walk(path):
    list_of_dirs = os.listdir(path)
    dirs_in_dir = []

    for item in list_of_dirs:
        a = os.path.join(path, item)
        if os.path.isdir(a):
            dirs_in_dir.append(item)

    if len(dirs_in_dir) == 0:
        print(f'{path}    :    path is empty.')
    else:
        print(f'{path}    :    {dirs_in_dir}')
        for directory in dirs_in_dir:
            new_path = os.path.join(path, directory)
            os_walk(new_path)


print(os_walk('/home/denis/PycharmProjects/beetroot_academy/unit_3'))
