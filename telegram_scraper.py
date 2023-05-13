import telebot
from telebot import types
import requests
import bs4
import json
import os
import urllib.request

bot = telebot.TeleBot(token='6165632559:AAFVM0lJu51Ty8p9sI6AmvhyIGJje0a0V6c')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book_downloader = types.KeyboardButton('📗 Download inform book')
    tmotor_downloader = types.KeyboardButton('🏍️ Tmotor prices')
    music_downloader = types.KeyboardButton('🎵 Ru Music Downloader')
    stop_download_music = types.KeyboardButton('🛑 Stop Downloading')

    markup.add(book_downloader, tmotor_downloader, music_downloader)

    bot.send_message(message.chat.id, 'Hello {0.first_name}! i am scraping bot'.format(message.from_user), reply_markup=markup)
    

    @bot.message_handler(content_types=['text'])
    def menu_scraping(message):
        if message.chat.type == 'private':
            if message.text == '📗 Download inform book':
                for i in range(1, 17):
                    file = open(f'inform/{i}.jpg', 'rb')
                    bot.send_photo(message.chat.id, file, f'{i}.png has been installed')
                    print(f'{i}.png has been sucsessfuly send!')



            if message.text == '🏍️ Tmotor prices':
                if not os.path.exists('motor_images'):
                    os.makedirs('motor_images')

                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
                }

                url = 'https://store.tmotor.com/category-2-b0-Motors.html'
                response = requests.get(url=url, headers=headers)
                soup = bs4.BeautifulSoup(response.content, 'html.parser')

                seria = soup.find_all('div', class_='w1201 floor-wrapper category-wrap')

                data = []

                for i in seria:
                    items = i.find('div', class_='mc').find('ul', class_='list-1')
                    for item in items:
                        if isinstance(item, bs4.element.Tag):
                            price = item.find('p').text.strip()
                            title = item.find('h5').find('a').text.strip()
                            data.append({'title': title, 'price': price})

                with open('prices.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                prices_json = open('prices.json', 'rb')
                bot.send_document(message.chat.id, prices_json)

            if message.text == '🎵 Ru Music Downloader':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                stop_download_music = types.KeyboardButton('🛑 Stop Downloading')
                markup.add(stop_download_music)
                bot.send_message(message.chat.id, 'Start downloading...', reply_markup=markup)
                for i in range(2, 100):
                    if message.text == '🛑 Stop Downloading':
                        break
                    url = f'https://dl5.ru-music.cc/mp3/{i}.mp3'
                    filename = url.split('/')[-1]
                    response = requests.get(url)
                    music = response.content
                    with open(f'music/{filename}', 'wb') as file:
                        file.write(music)
                    music = open(f'music/{i}.mp3', 'rb')
                    bot.send_document(message.chat.id, music)
                    print(f'{filename} is Downloaded!')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                stop_download_music = types.KeyboardButton('🛑 Stop Downloading')
                markup.add(stop_download_music)
                bot.send_message(message.chat.id, 'Downloading finished', reply_markup=markup)



bot.polling(none_stop=True)