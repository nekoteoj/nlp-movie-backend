from flask import current_app

from nlp_movie_backend.core.recommender import MovieRecomender
from nlp_movie_backend.util.singleton_container import singleton
from nlp_movie_backend.model import movie_repository


@singleton
def _get_recommender():
    return MovieRecomender(model_path=current_app.config.get("MODEL_PATH"),
                           metadata_path=current_app.config.get("META_PATH"))


def get_all():
    return movie_repository.get_all()


def get_by_text(text):
    recommender = _get_recommender()
    movies = recommender.recommend(text)
    scores, names = zip(*movies)
    movies = movie_repository.get_by_names(names)
    for i, movie in enumerate(movies):
        movie["score"] = scores[i].item()
    return movies
