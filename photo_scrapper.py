from bs4 import BeautifulSoup as bs
import requests

user_url = input("Please enter the url of the vsco image you would like to download: ")
response = requests.get(user_url)
soup = bs(response.text, 'html.parser')
images = soup.findAll('img')
for img in images:
    image_data = requests.get("https://" + img['src'][2:]).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(image_data)
