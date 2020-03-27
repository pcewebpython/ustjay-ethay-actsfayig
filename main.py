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


def translate_fact(fact):
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    payload = {'input_text': fact}
    translate = requests.post(url, data=payload, allow_redirects=False)
    return translate.headers.get('location')


@app.route('/')
def home():
    fact = get_fact()
    body = translate_fact(fact)
    link = '<a href="{}">{}</a>'.format(body, body)
    return Response(response=link, mimetype='text/html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

