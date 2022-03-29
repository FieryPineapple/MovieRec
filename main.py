from re import template
import re
from flask import Flask, render_template, request, redirect, url_for, session
import cg
from imdb import Cinemagoer
#from justwatch import JustWatch

app = Flask(__name__, template_folder = 'template')
app.config["DEBUG"] = True

#ia = cg.search()
cg = Cinemagoer()
#jw = JustWatch(country='US')

search_name = "keanu reeves"
search_type = "actor"
result_list = ""
name_list = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods = ['GET', 'POST'])
def search():
    #types = ['Actor/Actress', 'Movie', 'Director', 'Production Company']
    if request.method == 'POST':
        # search_type = request.form.get['choice']
        # search_name = request.form.get['search']
        # session["choice"] = search_type
        # session["search"] = search_name
        return redirect(url_for('results', search_type=search_type, search_name=search_name))
    return render_template('search.html')

@app.route('/results', methods = ['POST', 'GET'])
def results():
    # search_type = request.args.get("choice")
    # search_name = request.args.get("search")
    if request.method == 'POST':
        if search_type == 'actor':
            result_list = cg.search_person(search_name)
            for person in result_list:
                name = person['name']
                name_list.append(name)

        if search_type == 'movie':
            result_list = cg.search_movie(search_name)
            for movie in result_list:
                name = movie['title']
                name_list.append(name)
    
    return render_template('results.html', search_name=search_name, name_list=name_list)


@app.route('/mystuff')
def mystuff():
    return render_template('mystuff.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

app.run(host = "0.0.0.0")