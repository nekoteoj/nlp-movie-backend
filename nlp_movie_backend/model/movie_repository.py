import json
import random

from flask import current_app
from nlp_movie_backend.util.decorator import deepcopy, singleton


@deepcopy
@singleton
def _get_movies_from_json():
    with open(current_app.config.get("MOVIES_PATH")) as file_input:
        movies = json.load(file_input)
    return movies


@singleton
def _get_name_to_movie_map():
    movies = _get_movies_from_json()
    name_to_movie = {movie["name"]: movie for movie in movies}
    return name_to_movie


def get_all():
    return _get_movies_from_json()


def get_by_names(names):
    name_to_movie = _get_name_to_movie_map()
    return [name_to_movie[name.strip()] for name in names]
