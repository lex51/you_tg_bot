import requests
import yt_dlp
import os
from pprint import pprint as pp
from settings import Conf


test_video_url = 'https://www.youtube.com/watch?v=5ZOJhGIhqt8&ab_channel=ZProger%5BIT%5D'
api_ya_domen = 'https://functions.yandexcloud.net/d4eerai6vtlv7laen5nk'

# if __name__== "__main__":
# name  you_tg_bot
tg_token = Conf.tg_token

def download_audio(link):
    with yt_dlp.YoutubeDL(
        {
           'extract_audio': True, 
        #    'format': 'bestaudio', # worst
           'format': 'worstaudio',
          #  'audio-quality': 0, 
           'outtmpl': '%(title)s.mp3'
        }
    ) as video:
        info_dict = video.extract_info(link, download = True)
        # print(info_dict)
        video_title = info_dict['title']
        print(video_title)
        video.download(link)    
        # print("Successfully Downloaded - see local folder on Google Colab")

# def get_info(url):
#    with yt_dlp.YoutubeDL() as  video:
      

# download_audio(
#   'https://www.youtube.com/watch?v=cJuO985zF8E'
    # test_video_url
#   )
# curl \
#   --request POST \
#   --url https://api.telegram.org/bot<токен бота>/setWebhook?url=https://<Домен API-шлюза>/echo
url = f"https://api.telegram.org/bot{tg_token}/setWebhook?url={api_ya_domen}/echo"
resp = requests.post(
    url
)
pp(
    resp.content
)