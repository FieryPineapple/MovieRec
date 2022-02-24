from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello from Team Fiery Pineapple"

app.run(host = "0.0.0.0")
