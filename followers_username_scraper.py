import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/fredrex_57/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

followers_link = soup.find('a', class_='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd')

url_followers = f"https://www.instagram.com{followers_link}"
response_followers = requests.get(url_followers)
soup_followers = BeautifulSoup(response_followers.content, 'html.parser')

usernames = soup_followers.find_all('a', class_='FPmhX notranslate nJAzx')

data = []
for username in usernames:
    name = username.text
    data.append(name)

print(data)
