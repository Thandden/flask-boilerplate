from flask import Flask, g, session
from flask_htmx import HTMX

from app.blueprints.base import base
from app.database import init_db
from app.config.config import settings


def create_app() -> Flask:
    app = Flask(__name__)
    htmx = HTMX(app)
    init_db()
    app.config["SECRET_KEY"] = settings.SECRET

    @app.before_request
    def before_request():  # type: ignore
        """Make HTMX available for all routes"""
        g.htmx = htmx

    app.register_blueprint(base)
    return app
