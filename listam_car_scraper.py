import requests
from bs4 import BeautifulSoup
import json
from time import sleep

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

data = []

for i in range(2, 3):
    url = f"https://www.list.am/category/23/{i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    cars = soup.find('div', {'id': 'main'}).find('div', {'id': 'pagecol'}).find('div', {'id': 'contentr'}).find('div', class_='dl').find('div', class_='gl').find_all('a')

    for car in cars:
        sleep(0.1)
        price_elem = car.find('div', class_='p')
        title_elem = car.find('div', class_='l')
        description_elem = car.find('div', class_='at')
        image = car.find('img')['src']
        url = "https:" + image
        filename = url.split('/')[-1].replace(".webp", "") + ".jpg"
        response = requests.get(url)
        car_img = response.content

        if price_elem is not None and title_elem is not None and description_elem is not None:
            price = price_elem.text.strip()
            title = title_elem.text.strip()
            description = description_elem.text.strip()
            
            data.append({"title": title, "price": price, "description": description})
        with open(f"images/{filename}", 'wb') as file:
            file.write(car_img)

with open('cars_info.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
