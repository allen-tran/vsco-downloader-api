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

    for img in images:
        request_link = f"http:{img['src']}"
        image_data = requests.get(request_link).content
        with open('.\\static\\vsco_image.jpg', 'wb') as handler:
            handler.write(image_data)

    return jsonify({"link": request_link})
