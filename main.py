"""
For this week, you're going to be working on a mashup! You'll use the code to scrape a random
fact from http://unkno.com (Links to an external site.)Links to an external site. that we
developed in class, and send it to a pig latin web application running on Heroku. The address
of the Pig Latinizer is:
https://hidden-journey-62459.herokuapp.com/ (Links to an external site.)

The requirement is:

You should deploy your assignment to Heroku.
Whenever someone visits your home page, it should scrape a new fact from unkno.com, send that
fact to the pig latin website, and print out the address for that piglatinized fact on the home
page.

If you'd like to be fancy, then you can print the address as a clickable link.
"""

import os
import requests
from flask import Flask, render_template, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    """
    Return the random fact from http://unkno.com as a string.
    """
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_link(fact):
    """
    Feed the fact argument as a post to the pig latinizer, and return the resulting url.

    fact: the random fact from get_fact as a string.
    """
    payload = {'input_text': fact}
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
                             data=payload, allow_redirects=False)

    return response.headers['Location']


@app.route('/')
def home():
    fact = get_fact()
    link_ = get_link(fact)

    # return an html rendered response containing a hyperlink
    return render_template('response.jinja2', link=link_)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
