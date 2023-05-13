import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.roblox.com/home'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text

