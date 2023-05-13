import requests
from bs4 import BeautifulSoup
import urllib.request
import os

url = 'https://collabstr.com/influencers?p=instagram&c=lifestyle+Fashion+Beauty+Travel+Health+%26+Fitness+Food+%26+Drink+Model+Comedy+%26+Entertainment+Art+%26+Photography+Entrepreneur+%26+Business+Music+%26+Dance+Family+%26+Children+Animals+%26+Pets+Athlete+%26+Sports+Education+Adventure+%26+Outdoors+Celebrity+%26+Public+Figure+Actor+Gaming+&ct=united+states&l=Los+Angeles%2C+CA%2C+United+States&l_id=99001&pg=5'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

usernames = soup.find_all('div', class_='profile-listing-holder')

users = []

if not os.path.exists('images'):
    os.makedirs('images')

for user in usernames:
    image = user.find('div', class_='profile-listing-img-holder').img['src']
    filename = os.path.join('images', image.split('/')[-1])
    urllib.request.urlretrieve(image, filename)
