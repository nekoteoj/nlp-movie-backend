import os
import pathlib

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        MOVIES_PATH=os.path.join(pathlib.Path().absolute(), "data/movies.json"),
        SWAGGER={"title": "NLP Movie API", "uiversion": 3}
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    swagger = Swagger(app)
    CORS(app)

    from nlp_movie_backend.routes import movie

    app.register_blueprint(movie.bp)
    
    return app
