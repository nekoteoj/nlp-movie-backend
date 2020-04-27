import json
import random

from flask import current_app
from nlp_movie_backend.util.decorator import deepcopy, singleton
from nlp_movie_backend.model.db import get_db


def _map_movie_db_to_domain(movie_db):
    movie = dict()
    movie.update(movie_db["fields"])
    movie.update(
        {key: value
         for key, value in movie_db.items() if key != "fields"})
    return movie


def _get_movies_from_db():
    db = get_db()
    movies = db.get_all(fields=["name", "imageUrl"])
    return [_map_movie_db_to_domain(movie) for movie in movies]


def _get_movie_by_name_from_db(name):
    db = get_db()
    movie = db.match("name", name, fields=["name", "imageUrl"])
    return _map_movie_db_to_domain(movie)


def get_all():
    return _get_movies_from_db()


def get_by_names(names):
    return [_get_movie_by_name_from_db(name) for name in names]
