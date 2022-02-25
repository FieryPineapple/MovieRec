#Name: Qinyi Wang
#A3: Exercise 3

import json
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

books = [
    {'id': '0',
     'title': 'Pride and Prejudice',
     'author': 'Jane Austen',
     'genre': 'Romance',
     'year_published': '1813'
    },
    {'id': '1',
     'title': 'To Kill A Mockingbord',
     'author': 'Harper Lee',
     'genre': 'Southern Gothic',
     'year_published': '1960'
    },
    {'id': '2',
     'title': 'Of Mice and Men',
     'author': 'John Steinbeck',
     'genre': 'Social Realism',
     'year_published': '1937'
    },
    {'id': '3',
     'title': 'Frankenstein',
     'author': 'Mary Shelly',
     'genre': 'Gothic Fiction',
     'year_published': '1818'
    },
    {'id': '4',
     'title': 'Dracula',
     'author': 'Bram Stoker',
     'genre': 'Gothic Fiction',
     'year_published': '1897'
    }
]

@app.route('/all', methods=['GET'])
def all():
    return jsonify(books)

app.run(host = "0.0.0.0")