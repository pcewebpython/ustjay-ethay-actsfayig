import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def latinize(in_fact):

    ### latinize a supplied fact

    print(f"diag arg fact to latinize = -{in_fact}-")

    fact_to_latinize = in_fact

    # prepare the payload from form data, and initialize option allow_redirects off
    payload = {'input_text': fact_to_latinize}
    resource_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    r = requests.post(resource_url, data=payload, allow_redirects=False)

    # r contains the response from the latinizer api
    
    latinized_result_url = ""
    for key, value in r.headers.items():
        #print(f"diag  key = -{key}- value = -{value}-")
        pass
        
    try:
        # extract the location link from the response header
        latinized_result_url = r.headers['Location']
        #print(f"diag latinized_result_url = -{latinized_result_url}-")
    except Exception as err:
        latinized_result_url = ""
        #print(f'diag latinizer error occurred: {err}')
        pass

    # prepare the result (url to latinized result)
    result = r.text
    if latinized_result_url != "":
        result = latinized_result_url
        
    return result

    
def get_random_fact():

    ### get a random fact from unkno api
    
    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    random_fact = facts[0].getText()

    #print(f"diag a random fact = -{random_fact}-")
   
    return random_fact

    
def do_latinize_a_random_fact():

    ### latinize a random fact control
    
    random_fact = get_random_fact()
    latinized_fact = latinize(random_fact)
    
    return latinized_fact

    
@app.route('/')
def home():
    body = do_latinize_a_random_fact()
    return body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

