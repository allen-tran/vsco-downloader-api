from flask import Flask, request, render_template, redirect
import photo_scrapper
import video_scrapper

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/fetch', methods=["POST"])
def home_form():
    print(request.form)
    user_url = request.form['text']
    print(user_url)
    response_link = video_scrapper.scrape_video(user_url)
    if response_link:
        return

    response_link = photo_scrapper.scrape_photo(user_url)

    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
