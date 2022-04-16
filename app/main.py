from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from imdb import Cinemagoer
from . import db

main = Blueprint('main', __name__)

cg = Cinemagoer()

name = ""
type = ""
resultList = ""
nameList = []

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/movies')
def movies():
    return render_template('movies.html')

@main.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@main.route('/results', methods = ['POST', 'GET'])
def results():
    type = request.form.get("choice")
    name = request.form.get("search")

    if request.method == 'POST':
        if type == 'actor':
            resultList = cg.search_person(name)
            for person in resultList:
                n = person['name']
                nameList.append(n)

        if type == 'movie':
            resultList = cg.search_movie(name)
            for movie in resultList:
                n = movie['title']
                nameList.append(n)
    
    return render_template('results.html', sname=name, nameList=nameList)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)