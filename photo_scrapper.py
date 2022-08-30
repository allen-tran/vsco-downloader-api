from bs4 import BeautifulSoup as bs
import requests
import time
from flask import jsonify


def scrape_photo(user_url):
    response = requests.get(user_url)
    soup = bs(response.text, 'html.parser')
    images = soup.findAll('img')

    if not images:
        return None

    filename = generate_time()
    for img in images:
        request_link = f"http:{img['src']}"
        image_data = requests.get(request_link).content
        with open(filename, 'wb') as handler:
            handler.write(image_data)

    return jsonify({"link": request_link})


def generate_time():
    return f"{time.time()}.jpg"
