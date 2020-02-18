# Написать скрипт, который будет удалять файл из каталога. Запустить скрипт из консоли с аргументами указывающими
# какой файл удалить и из какого каталога (директории).

# /home/denis/PycharmProjects/beetroot_academy/unit_3/lesson_19/presentation       test_file.txt


import os
import sys
import argparse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Написать свой Formatter для логгера с заменой \n на !!!\n
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s!!!')

file_handler = logging.FileHandler('/home/denis/PycharmProjects/beetroot_academy/unit_3/lesson_19/presentation/'
                                   'logger_1.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('Process is running')


os.mknod('/home/denis/PycharmProjects/beetroot_academy/unit_3/lesson_19/presentation/test_file.txt')
logger.debug('File "test_file.txt" was created')


parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
parser.add_argument('file_del', type=str)
logger.debug('Arguments from the terminal are parsed')


args = parser.parse_args()

file_path = os.path.join(args.path, args.file_del)
logger.debug('File path was set')

# В скрипт из предыдущего задания добавить проверку версии Python
# Если версия < 3.7 - создавать пустой файл, вместо удаления.

python_version = sys.version_info[:2]
logger.info('Interpreter version is defined.')

if python_version[0] == 3 and python_version[1] >= 7:
    os.mknod('/home/denis/PycharmProjects/beetroot_academy/unit_3/lesson_19/presentation/test_version_file.txt')
    logger.info('File "test_version_file.txt" was created.')
else:
    os.remove(file_path)
    logger.info('File "test_file.txt" was removed')


# В этом же скрипте проверить количество ядер CPU и если их меньше 4 - завершать работу скрипта
# с исключением SystemExit.

count_of_cpu = os.cpu_count()

if count_of_cpu < 4:
    logger.warning("Count of CPU's is not 4!")
    sys.exit("SystemExit")



