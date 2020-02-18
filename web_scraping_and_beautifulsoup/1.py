# Отправить запрос на розетку и достать информацию об определенной группе товаров: цена, картинка, ссылка.

import requests
from bs4 import BeautifulSoup


url = 'https://rozetka.com.ua/notebooks/c80004/'

response = requests.get(url)
response_content = response.content

bs_obj = BeautifulSoup(response_content, features='html.parser')
my_div = bs_obj.find_all('div', class_='goods-tile')


s_images = []
s_titles = []
s_prices = []


# картинка товара
for div in my_div:
    images = div.find_all('a', class_='goods-tile__picture')
    for image in images:
        link = image.get('href')
        s_images.append(link)

# название товара
for div in my_div:
    names = div.find_all('a', class_='goods-tile__heading')
    for name in names:
        title = name.get('title')
        s_titles.append(title)

# цена товара
for div in my_div:
    prices = div.find_all('span', 'goods-tile__price-value')
    for price in prices:
        s_prices.append(price.contents[0])


i = 0
while i != len(s_images):
    print(f'Notebook: {s_titles[i]}.\n'
          f'Price: {s_prices[i]}.\n'
          f'Photo: {s_images[i]}.\n')
    i += 1
