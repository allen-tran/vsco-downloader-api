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
        print(vid)
        video_data = requests.get("https:" + vid['src']).content

        filename = generate_time()
        with open(filename, 'wb') as handler:
            handler.write(video_data)
    return 1


def generate_time():
    return f"{time.time()}.mp4"
