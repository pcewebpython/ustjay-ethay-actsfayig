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

def latinize(in_fact):

    print(f"***MMM arg fact to latinize = -{in_fact}-")

    #***MMM
    #fact_to_latinize = in_fact
    fact_to_latinize = 'test'

    payload = {'input_text': fact_to_latinize}
    #resource_url = "https://hidden-journey-62459.herokuapp.com/"
    #r = requests.post(resource_url, data=payload, allow_redirects=False)
    
    resource_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    r = requests.post(resource_url, data=payload, allow_redirects=False)

    print(f"***MMM response text = -{r.text}-")

    for key, value in r.headers.items():
        print(f"***MMM 111111111111 key = -{key}- value = -{value}-")
    
    try:
        #latinized_result_url = r.headers['content-type']
        latinized_result_url = r.headers['Location']
        print(f"***MMM latinized_result_url = -{latinized_result_url}-")
    except Exception as err:
        print(f'***MMM 555555555555555555555Other error occurred: {err}')

    print(f"***MMM 333333333333333333333")
        
    
 
    #soup = BeautifulSoup(response.content, "html.parser")
    #facts = soup.find_all("div", id="content")

    #print(f"***MMM facts = -{facts[0].getText()}-")
    
    return r.text

    
def get_random_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    random_fact = facts[0].getText()

    print(f"***MMM a random fact = -{random_fact}-")
   
    return random_fact

def do_latinize_a_random_fact():

    random_fact = get_random_fact()
    latinized_fact = latinize(random_fact)
    
    return latinized_fact
    #return "hello mike"


@app.route('/')
def home():

    print("***MMM aaaaaaaaaaaa")
    body = do_latinize_a_random_fact()
    
    #print(f"***MMM called result fact = -{facts[0].getText()}-")
    
    #return "FILL ME!"
    return body


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

