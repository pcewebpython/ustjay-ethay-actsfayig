import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

###
###//hidden-journey-62459.herokuapp.com/piglatinize/
### r = requests.post('https://httpbin.org/post', data = {'key':'value'})
###
#payload = {'key1': 'value1', 'key2': 'value2'}
#>>> r = requests.post("https://httpbin.org/post", data=payload)
#>>> print(r.text)

def get_fact():

    payload = {'input_text': 'test'}

    #resource_url = "https://hidden-journey-62459.herokuapp.com/"
    #r = requests.post(resource_url, allow_redirects=False, data=payload)
    
    resource_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    r = requests.post(resource_url, allow_redirects=True, data=payload)

    print(f"***MMM response text = -{r.text}-")

    #soup = BeautifulSoup(response.content, "html.parser")
    #facts = soup.find_all("div", id="content")

    #print(f"***MMM facts = -{facts[0].getText()}-")
    
    return r.text

    
def get_fact_00():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    print(f"***MMM facts = -{facts[0].getText()}-")
    
    return facts[0].getText()


@app.route('/')
def home():

    print("***MMM aaaaaaaaaaaa")
    result_fact = get_fact()
    
    #print(f"***MMM called result fact = -{facts[0].getText()}-")
    
    #return "FILL ME!"
    return result_fact


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

