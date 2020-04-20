import json
import random

from flask import current_app

MOVIES = None
def _get_movies_from_json():
    global MOVIES
    if MOVIES is None:
        with open(current_app.config.get("MOVIES_PATH")) as file_input:
            MOVIES = json.load(file_input)
    return MOVIES

def get_all():
    return _get_movies_from_json()

def get_by_text(text):
    return random.sample(_get_movies_from_json(), 5)
