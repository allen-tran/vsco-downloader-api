from bs4 import BeautifulSoup as bs
import requests
import time

def scrape_photo(user_url):
    response = requests.get(user_url)
    soup = bs(response.text, 'html.parser')
    images = soup.findAll('img')

    if not images:
        return None

    filename = generate_time()
    for img in images:
        image_data = requests.get("https://" + img['src'][2:]).content
        with open(filename, 'wb') as handler:
            handler.write(image_data)

    return 1



def generate_time():
    return f"{time.time()}.jpg"
