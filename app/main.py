from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from imdb import Cinemagoer
import json
from .models import User
from . import db

main = Blueprint('main', __name__)

cg = Cinemagoer()

name = ""
type = ""
resultList = ""
image = ""
myList = []
searchList = {}
sName = []
sID = []

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/movies')
def movies():
    chart = cg.get_popular100_movies()
    chart = chart[0:20]
    return render_template('movies.html', chart=chart)

@main.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template('search.html')

@main.route('/results', methods = ['POST', 'GET'])
def results():

    type = request.form.get("choice")
    name = request.form.get("search")

    if request.method == 'POST':
        #Clear dictionary values
        #for value in searchList.values():
        #    del value[:]

        searchList.clear()
        sName.clear()
        sID.clear()

        count = 1
        
        if type == 'actor':
            resultList = cg.search_person(name)
            for person in resultList:
                searchList[count] = {"ID": "", "Name": ""}
                id = person.getID()
                sID.append(id)
                searchList[count]['ID'] = id
                n = person['name']
                searchList[count]['Name'] = n
                #searchList['ID'].append(id)
                sName.append(n)
                count += 1
                #searchList['Name'].append(n)

        if type == 'movie':
            resultList = cg.search_movie(name)
            for movie in resultList:
                n = movie['title']
                #searchList.append(n)

        if type == 'director':
            resultList = cg.search_person(name)
            for person in resultList:
                n = person['name']
                #searchList.append(n)

        if type == 'company':
            resultList = cg.search_company(name)
            for company in resultList:
                n = company['name']
                #searchList.append(n)
    
    return render_template('results.html', name=name, sName = sName, sID = sID, searchList=searchList)

@main.route('/information', methods = ['POST', 'GET'])
def information():
    person = "0000206"
    bio = ""
    other = ""
    #selection = request.form.get("selection")
    #if request.method == 'POST':
    b = cg.get_person(person, info=['biography'])
    name = "Keanu Reeves"
    bio = b.get('biography', [])
    bio = ''.join(bio)
    o = cg.get_person(person, info=['other works'])
    other = o.get('other works', [])

    updatedList = json.dump(myList)
    db.session.add(updatedList)
    
    return render_template('information.html', bio=bio, other=other, name=name)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)