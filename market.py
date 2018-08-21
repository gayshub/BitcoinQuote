
# -*- coding: utf-8 -*-



from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)
import json


@app.route('/')
def hello_world():
    r = requests.get('http://market.jinse.com/api/v1/currency/ranks')
    hjson = json.loads(r.text)
    return render_template('hello.html',arr=hjson)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
