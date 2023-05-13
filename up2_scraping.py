import requests
from bs4 import BeautifulSoup
import urllib.request
import os

url = 'https://www.walmart.ca/cp/grocery'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

images = soup.find('div', class_='css-1kst9ea e1s46ex60') \
             .find('div', class_='css-1uqs17u e1r0e0t90') \
             .find('div', class_='css-hqry55 eaue1ee2')

if not os.path.exists('images'):
    os.makedirs('images')

for i, image in enumerate(images):
    url = image.find('img')['src']
    extension = os.path.splitext(url)[-1]
    filename = f'image_{i}{extension}'
    filepath = os.path.join('images', filename)
    urllib.request.urlretrieve(url, filepath)
    print(f'Downloaded {filename}')
