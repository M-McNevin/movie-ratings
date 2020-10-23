"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server


os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
    for movie in movie_data:
        title = movie_data['title'] 
        overview = movie_data['overview'] 
        datetime.strptime(movie_data['release_date'], %Y-%m-%d ) = movie_data['release_date'] 
        poster_pathmovie_data= ['poster_path'] 

        movies_in_db.append(title,overview,release_date,poster_path)

    return movies_in_db

# movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)