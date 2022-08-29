from re import L
from flask import Flask, Response, request, jsonify
import json
import photo_scrapper
import video_scrapper

app = Flask(__name__)


@app.route('/')
def home():
    return Response(status=200, mimetype='application/json')


@app.route("/fetchObject/", methods=["POST"])
def scrape():
    user_url = request.json
    print(user_url['link'])

    if video_scrapper.scrape_video(user_url['link']):
        return

    photo_scrapper.scrape_photo(user_url['link'])

    return Response(status=201, mimetype='application/json')


if __name__ == "__main__":
    app.run(port=7777)
