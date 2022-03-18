from re import template
import re
from flask import Flask, render_template, request, redirect, url_for, session
import cg
from imdb import Cinemagoer
#from justwatch import JustWatch

application = Flask(__name__, template_folder = 'template')
application.config["DEBUG"] = True

#ia = cg.search()
cg = Cinemagoer()
#jw = JustWatch(country='US')

search_name = "keanu reeves"
search_type = "Actor/Actress"
result_list = ""
name_list = []

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/search', methods = ['GET', 'POST'])
def search():
    types = ['Actor/Actress', 'Movie', 'Director', 'Production Company']
    # if request.method == 'POST':
    #     search_type = request.form.get['types']
    #     search_name = request.form.get['search']
    #     session["types"] = search_type
    #     session["search"] = search_name
    #     return redirect(url_for('results', search_type=search_type, search_name=search_name))
    return render_template('search.html', types=types)

@application.route('/results', methods = ['POST'])
def results():
    # search_type = session["types"]
    # search_name = session["search"]
    if request.method == 'POST':
        if search_type == 'Actor/Actress':
            result_list = cg.search_person(search_name)
            for person in result_list:
                name = person['name']
                name_list.append(name)

        if search_type == 'Movie':
            result_list = cg.search_movie(search_name)
            for movie in result_list:
                name = movie['title']
                name_list.append(name)
    
    return render_template('results.html', search_name=search_name, name_list=name_list)


@application.route('/mystuff')
def mystuff():
    return render_template('mystuff.html')

@application.route('/movies')
def movies():
    return render_template('movies.html')

application.run(host = "0.0.0.0",port=8080)
