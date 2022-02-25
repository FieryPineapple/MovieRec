from flask import Flask
import json

app = Flask(__name__)

basketball_cards = [
  {
    "name" : "Lebron James",
    "price" : 129.99
  },
  {
    "name" : "Alex Caruso",
    "price" : 24.99
  },
  {
    "name" : "Chris Paul",
    "price" : 54.99
  }
]

@app.route("/search/<max_salary>")
def search_salary(max_salary):
  max_salary = float(max_salary)
  res = []
  for player in basketball_cards:
    if player["price"] <= max_salary:
      res.append(player)
  return json.dumps(res)

app.run(host = "0.0.0.0")
