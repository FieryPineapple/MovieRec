from flask import Flask, request

app = Flask(__name__)
#app.config["DEBUG"] = True

person = input("Enter your name: ")

@app.route('/welcome', methods = ["GET"])
def greeting_msg():
    return ("Hi! Welcome to this page " + person + " :)")

app.run(host = "0.0.0.0")
