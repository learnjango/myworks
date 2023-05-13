import requests
import bs4
import json
import os
import urllib.request


if not os.path.exists('motor_images'):
    os.makedirs('motor_images')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

url = 'https://store.tmotor.com/category-2-b0-Motors.html'
response = requests.get(url=url, headers=headers)
soup = bs4.BeautifulSoup(response.content, 'html.parser')

seria = soup.find_all('div', class_='w1201 floor-wrapper category-wrap')

data = []

for i in seria:
    items = i.find('div', class_='mc').find('ul', class_='list-1')
    for item in items:
        if isinstance(item, bs4.element.Tag):
            price = item.find('p').text.strip()
            title = item.find('h5').find('a').text.strip()
            data.append({'title': title, 'price': price})

with open('prices.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
