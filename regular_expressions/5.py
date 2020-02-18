# Разбить строку по нескольким разделителям : , пробел
import re


lorem = 'Lorem ipsum: dolor sit ---  amet, consectetur: adipiscing elit. In a tortor ut: est pulvinar suscipit. Duis '

result = re.findall(r'[^:, ]+', lorem)
print(result)