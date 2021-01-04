"""a simple app to serve up pig latin"""

import os
import requests
from flask import Flask, send_file, Response, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
FACT_URL = 'http://unkno.com'
PIG_LATINIZER_URL = 'http://hidden-journey-62459.herokuapp.com/piglatinize'

def get_fact():
    """ get the pig latin """

    response = requests.get(FACT_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    pig_latin_prhase = facts[0].getText().strip()

    return pig_latin_prhase


@app.route('/')
def home():
    """main functionality"""

    my_fact = get_fact()
    fact_dict = {'input_text': my_fact}
    print(fact_dict)
    pig_latin_response = requests.post(PIG_LATINIZER_URL,
                                       allow_redirects=False,
                                       data=fact_dict)
    print(pig_latin_response.headers)
    pig_latin_location = pig_latin_response.headers['Location']
    print('test_' + pig_latin_location)
    pig_latin_url = f'<a href="{pig_latin_location}">{pig_latin_location}</a>'
    return render_template('pig_latin_translator.jinja2', pig_latin=pig_latin_url)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    # app.run(host='0.0.0.0', port=port) # heroku
    app.run(host='localhost', port=port) # local

