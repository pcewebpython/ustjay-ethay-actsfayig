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

def get_pig_latin(url):
    response = requests.get(url)
    split_text = response.text.split('\n')
    return_text = split_text[8].strip()
    return return_text

@app.route('/')
def home():
    phrase = get_fact().strip()
    punctuation = phrase[-1:]
    data = {'input_text': phrase[:-1],}
    response = requests.post(url="https://fierce-mountain-23253.herokuapp.com/", data=data)
    pig_response = get_pig_latin(response.url)
    return pig_response + punctuation


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)