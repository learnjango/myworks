import requests
from bs4 import BeautifulSoup
import json

page = 2
for i in range(10):
    page += 1
    url = 'https://shamshyan.com/hy/category/gagik-shamshyan?page=111'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h5', class_='xfont-extrabold text-white')
    print(articles)

    data = []
    for article in articles:
        title = article.text
        data.append({'title': title})


    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)