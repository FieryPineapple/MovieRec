from flask import Flask
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["DEBUG"] = True

rq = Request('https://www.nytimes.com/')
response = urlopen(rq).read()

soup = BeautifulSoup(response, features="html.parser")

title = soup.title.text

@app.route('/qw')
def qw():
    return title

app.run(host = "0.0.0.0")