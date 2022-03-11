import unittest
from imdb import Cinemagoer

cg = Cinemagoer()
person = cg.search_person('keanu reeves')
movie = cg.search_movie('matrix')

class Test(unittest.TestCase):
    def test_actor_search(self):
        self.assertEqual(person[0]['name'], 'Keanu Reeves')
        self.assertEqual(person[3]['name'], 'Keanu Reeves')
    
    def test_movie_search(self):
        self.assertEqual(movie[0]['title'], 'The Matrix')
        self.assertEqual(movie[4]['title'], 'The Matrix')
        self.assertRegexpMatches(movie[4]['title'], 'Matrix')

if __name__ == '__main__':
    unittest.main()



"""
#Check list
for p in person:
    print(p['name'])

for m in movie:
    print(m['title'])
""" 