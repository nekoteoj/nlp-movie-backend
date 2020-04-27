import airtable

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = airtable.Airtable(
            base_key=current_app.config["AIRTABLE_BASE_KEY"],
            api_key=current_app.config["AIRTABLE_API_KEY"],
            table_name="Movie")

    return g.db


def close_db(e=None):
    db = g.pop('db', None)


def init_app(app):
    app.teardown_appcontext(close_db)
