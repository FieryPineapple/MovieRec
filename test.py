import unittest
from imdb import Cinemagoer
from justwatch import JustWatch

cg = Cinemagoer()
person = cg.search_person('keanu reeves')
movie = cg.search_movie('matrix')

jw = JustWatch()
movie_providers = jw.get_providers()



class Test(unittest.TestCase):
    def test_actor_search(self):
        self.assertEqual(person[0]['name'], 'Keanu Reeves')
        self.assertEqual(person[3]['name'], 'Keanu Reeves')
    
    def test_movie_search(self):
        self.assertEqual(movie[0]['title'], 'The Matrix')
        self.assertEqual(movie[4]['title'], 'The Matrix')
        self.assertRegexpMatches(movie[4]['title'], 'Matrix')

    def test_movie_provider_name(self):
        self.assertEqual(movie_providers[0]["technical_name"], "netflix")
    
    
    def test_available_movie_providers(self):
          self.assertNotIn("Hulu", movie_providers) # Hulu is currently not listed as one of the streaming services

if __name__ == '__main__':
    unittest.main()



"""
#Check list
for p in person:
    print(p['name'])

for m in movie:
    print(m['title'])
""" 