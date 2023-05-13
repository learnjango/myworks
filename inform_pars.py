import requests
import os

if not os.path.exists('inform'):
    os.mkdir('inform')

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

for i in range(1, 163):
    url = f"https://online.fliphtml5.com/fumf/yxin/files/thumb/{i}.jpg"
    req = requests.get(url, headers=headers)
    response = req.content

    with open(f"inform/{i}.jpg", 'wb') as file:
        file.write(response)
        print(f'[+] Image {i} has been downloaded!')
print('Done!')