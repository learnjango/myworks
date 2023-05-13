from TikTokApi import TikTokApi
import urllib.request

api = TikTokApi()

# Получаем первые 10 популярных видео на TikTok
trending_videos = api.trending.videos()

for video in trending_videos:
    # Получаем ссылку на видео
    video_url = video["video"]["downloadAddr"]
    # Скачиваем видео с помощью библиотеки urllib
    urllib.request.urlretrieve(video_url, f"{video['id']}.mp4")
