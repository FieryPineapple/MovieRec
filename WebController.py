from flask import Flask
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import math

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

@app.route('/rc', methods = ["GET"])
def rc():
    user_num1 = int(input("Enter first number: "))
    user_num2 = int(input("Enter second number: "))
    result = math.gcd(user_num1, user_num2)
    return ("The greatest common divisor of " + str(user_num1) + " and " + str(user_num2) + " is " + str(result))


app.run(host = "0.0.0.0")
