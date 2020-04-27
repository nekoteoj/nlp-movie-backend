import os
import pathlib

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(pathlib.Path().absolute(), ".env"))


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SWAGGER={
                                "title": "NLP Movie API",
                                "uiversion": 3
                            },
                            MODEL_PATH=os.path.join(pathlib.Path().absolute(),
                                                    "resource/model.h5"),
                            META_PATH=os.path.join(pathlib.Path().absolute(),
                                                   "resource/meta.pkl"),
                            AIRTABLE_API_KEY=os.getenv("AIRTABLE_API_KEY"),
                            AIRTABLE_BASE_KEY=os.getenv("AIRTABLE_BASE_KEY"))

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

    from nlp_movie_backend.model import db

    db.init_app(app)

    return app
