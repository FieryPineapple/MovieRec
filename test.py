import unittest
from imdb import Cinemagoer

class Test(unittest.TestCase):
    def test_search(self):
        cg = Cinemagoer()
        person = cg.search_person('keanu reeves')