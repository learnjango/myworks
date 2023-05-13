from bs4 import BeautifulSoup
import urllib.request

class Parser:
    html = ''
    raw_html = ''
    result = []

    def __init__(self, url, path):
        self.url = url
        self.path = path
    

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        html = req.read()
        soup = BeautifulSoup(html, features=html)
    
    def run(self):
        self.get_html()