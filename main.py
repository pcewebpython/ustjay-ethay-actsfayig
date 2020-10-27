#!/usr/bin/env python
"""
# ------------------------------------------------------------------------ #
# Title: Lesson 5 - Mashups & Microservices.  This script demonstrates
# how to scrape a random fact from http://unkno.com (Link to an external site)
# and then send it to a pig latin web application running on Heroku.
# Description: This is the main "main.py" script.  Use this command 'python -u main.py'
# to start the server.
# ChangeLog (Who,When,What):
# ASimpson, 10/27/2020, Modified code to complete lesson5 - Assignment05
# ------------------------------------------------------------------------ #
"""

import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    """Get the ransom factoid from this website http://unkno.com"""
    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def pig_latinizer(message):
    '''pig latin address function generator'''
    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data ={'input_text': message}, allow_redirects=False, stream=True)
    pig_latin_message = response.headers['Location']
    return pig_latin_message

@app.route('/')
def home():
    """Take a random fact from one website, convert it to Pig Latin and then show the address"""
    str_fact_message = str(get_fact())
    str_pig_latin_addr = pig_latinizer(str_fact_message)
    response_body = '<h1>Crazy Factoid:  <p style="font-size:18px;color:red"><i>"{0}"</i></p></h1>' \
                    '<h3>Convert this to Pig Latin (addr) ===>  <b>{1}</h3><br>' \
                    '<a href="{1}">Click here for Pig Latin version!!</a>'.format(str_fact_message, str_pig_latin_addr)
    return response_body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

