import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


data = {'input_text': get_fact()}

@app.route('/')
def home():
    response = requests.post(
        "https://hidden-journey-62459.herokuapp.com/piglatinize/", data, allow_redirects=False)
    page_headers = response.headers
    pig_url = page_headers['Location']
    return pig_url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

