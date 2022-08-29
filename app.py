from re import L
from flask import Flask
import json
app = Flask(__name__)
import photo_scrapper
import video_scrapper

@app.route('/')
def home():
    return json.dumps({'hello': 'hello'})

@app.route("/download/", methods=["GET", "POST"])
def scrape():
    user_url = input("Please enter the url of the vsco image you would like to download: ")

    if not photo_scrapper.scrape_photo(user_url):
        return
    
    video_scrapper.scrape_video(user_url)

if __name__ == "__main__":
    app.run(port=7777)