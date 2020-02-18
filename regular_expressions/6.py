# Из файла https://docs.google.com/document/d/1yB9ANOJnIFbdt5CWnUyPTuiN2zsZfYf3ssmwVwjdxzE/edit?usp=sharing найти
# следующую информацию: ['domain_name', 'domain__id', 'registrar', 'registrar_url', 'registrar_id', 'registrar_email',
# 'registrar_phone', 'status', 'registrant_id', 'registrant_name', 'registrant_address', 'registrant_city',
# 'registrant_state_province', 'registrant_postal_code', 'registrant_country']


import re


with open('cybercity.txt', 'r') as file:
    text = file.read()

# pattern = re.compile(r'(?<=Domain Name: )[A-Z]+\.[A-Z]+')
# pattern = re.compile(r'(?<=Registry Domain ID: )[A-Z0-9]+-[A-Z]+')
# pattern = re.compile(r'(?<=Registrar WHOIS Server: )\w+\.\w+\.\w+')
# pattern = re.compile(r'(?<=Registrar URL: )http://www.?\w+\.\w+')
# pattern = re.compile(r'(?<=Registrar IANA ID: )\d+')
# pattern = re.compile(r'(?<=Contact Email: )\w+@\w+\.\w+')
# pattern = re.compile(r'(?<=Contact Phone: )\+\d+\.\d+')
# pattern = re.compile(r'(?<=Domain Status: )\w+\s.+')
# pattern = re.compile(r'(?<=Registrant ID: )[A-Z0-9]+')
# pattern = re.compile(r'(?<=Registrant Name: )[A-Z]\w+\s[A-Z]\w+')
# pattern = re.compile(r'(?<=Registrant Street: )(([A-Z]\w+[A-Z]\w+[A-Z]\w+\.\w{3})|(\d+\s[A-Z]\.\s[A-Z]\w+\s[A-Z]\w+))')
pattern = re.compile(r'(?<=Registrant Street: ).+')



my_subs = pattern.findall(text)
print(my_subs)
