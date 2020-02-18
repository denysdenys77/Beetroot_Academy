# Провалидировать список емейлов, в каждом эмейле должен присутствовать символ @ и доменное имя после точки


import re


e_mails = 'info@senior.ua, y.mincheva@voxukraine.org, Zaporizhzhia@dabi.gov.ua'

result = re.findall(r'\w+@\w+\.\w+', e_mails)
print(result)