# returns movie details
import random
from imdb import IMDb


def imdb_bot():
    moviesDB = IMDb()
    try:
        print("Please make sure you have connected to internet")
        name = input("Please enter a movie name: ")
        movies = moviesDB.search_movie(name)
        idd = movies[0].getID()
        movie = moviesDB.get_movie(idd)

        print("movie:", movie['title'])
        print("year:", movie['year'])
        print("rating:", movie['rating'])
        casting = movie['cast']
        actors = ','.join(map(str, casting[0:10]))

        print("actors:", actors)
        print("------------------------")
    except:
        print("Please enter a valid movie name")
