from flask import Blueprint, jsonify, request

from nlp_movie_backend.service import movie_service


bp = Blueprint("movie", __name__, url_prefix="/movie")


@bp.route("/text")
def get_movies_by_text():
    """
    Get movie by a text query endpoint
    ---
    tags:
      - movies
    parameters:
      - in: query
        name: query
        schema:
            type: string
        required: true
        description: Query text of movies to get
    responses:
        '200':
            description: List of movies matched with query
    """
    text = request.args.get("query")
    movies = movie_service.get_by_text(text)
    return jsonify(movies=movies)


@bp.route("/")
def get_all_movies():
    """
    Get all movies endpoint
    ---
    tags:
      - movies
    responses:
        '200':
            description: List of all movies
    """
    movies = movie_service.get_all()
    return jsonify(movies=movies)
