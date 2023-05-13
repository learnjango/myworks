import fake_useragent
import requests
import time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}

response = requests.post('https://www.wildberries.ru/webapi/lk/mobile/requestconfirmcode?forAction=EasyLogin', headers=headers, json={'confirmCode': "153985", 'country': "AM", 'deviceId': "1673444226115z8puERz", 'osType': "Web", 'phoneNumber':  37498985294})
print('Send')
