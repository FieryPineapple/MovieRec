from flask import Flask
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config["DEBUG"] = True

rq = Request('https://www.nytimes.com/')
response = urlopen(rq).read()

soup = BeautifulSoup(response, features="html.parser")

title = soup.title.text

@app.route('/qw')
def qw():
    return title

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"password123")

@app.route('/alex')
def alex():
  return token

app.run(host = "0.0.0.0")
