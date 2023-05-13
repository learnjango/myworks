import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('music'):
    os.mkdir('music')

for i in range(2, 100):
    url = f'https://dl5.ru-music.cc/mp3/{i}.mp3'
    filename = url.split('/')[-1]
    response = requests.get(url)
    music = response.content
    with open(f'music/{filename}', 'wb') as file:
        file.write(music)
    print(f'{filename} is Downloaded!')
