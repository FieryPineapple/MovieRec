# Alma Campos
# A3 Exercise 3

from flask import Flask
import json

app = Flask(__name__)

members = [
  {
    "first_name" : "Alexander",
    "last_name" :   "Lee"
  },
  {
    "first_name" : "Alma",
    "last_name" :   "Campos"    
  },
  {
    "first_name" : "Rosalinda",
    "last_name" :   "Chamale" 
  },
  {
    "first_name" : "Qinyi",
    "last_name" :   "Wang"
  }
]

@app.route('/team')
def team():
    return json.dumps(members)

@app.route('/welcome')
def welcome():
    return "Welcome from the Fiery Pineapple"


app.run(host = "0.0.0.0")