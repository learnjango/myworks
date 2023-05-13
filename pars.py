import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import json

url = 'https://q-parser.ru/catalog'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

find_block = soup.find('div', class_='main').find_all('div', class_='item-list-item')

data = []

for block in find_block:
    image = block.find('div', class_='item-image').img['src']
    name = block.find('div', class_='item-title').find('a', class_='title').text
    data.append({'title': name})
    filename = os.path.join('images', image.split('/')[-1])
    urllib.request.urlretrieve(image, filename)

with open('names.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
