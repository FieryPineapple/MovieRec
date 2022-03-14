from re import template
from flask import Flask, render_template, request
import cg
from imdb import Cinemagoer
#from justwatch import JustWatch

app = Flask(__name__, template_folder = 'template')
app.config["DEBUG"] = True

ia = cg.search()
#jw = JustWatch(country='US')

@app.route('/')
def home():
    return render_template('home.html')
    #return "Welcome"

@app.route('/search', methods = ['GET', 'POST'])
def search():
    name = request.args.get('text')
    types = ['Actor/Actress', 'Movie', 'Director', 'Production Company']
    return render_template('search.html', types=types)
    #return actor_name

app.run(host = "0.0.0.0")