from time import time
from bs4 import BeautifulSoup as bs
import requests
import time


def scrape_video(user_url):

    response = requests.get(user_url)
    soup = bs(response.text, 'html.parser')
    videos = soup.findAll('source')

    if not videos:
        return None

    for vid in videos:
        request_link = "http:" + vid['src']
        video_data = requests.get(request_link).content

        filename = generate_time()
        with open(filename, 'wb') as handler:
            handler.write(video_data)
    return {"link": request_link}


def generate_time():
    return f"{time.time()}.mp4"
