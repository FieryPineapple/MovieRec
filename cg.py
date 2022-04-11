from imdb import Cinemagoer

cg = Cinemagoer()

person = cg.search_person("julia")
for p in person:
    print(p['name'])
    print(p.getID())

class search:
    # actor_name = input("Enter the name of the actor: ")
    # movie_name = input("Enter the name of the")

    def actor_search(actor_name):
        person = cg.search_person(actor_name)
        for p in person:
            print(p['name'])

    def movie_search(movie_name):
        movie = cg.search_movie(movie_name)
        for m in movie:
            print(m['title'])

#actor_search(actor_name)