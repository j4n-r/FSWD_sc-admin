import os
from datetime import timedelta
from logging.config import dictConfig

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from werkzeug.routing import Rule

from app.api import api_bp
from app.auth import auth_bp
from app.main import main_bp


def create_app(test_config=None):
    load_dotenv()

    # https://flask.palletsprojects.com/en/stable/logging/#basic-configuration
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)
    DB_URL = os.getenv("DB_URL")
    if DB_URL == None:
        DB_URL = "instance/db.sqlite3"

    app.logger.info(f"DB_URL: {DB_URL}")
    app.config.from_mapping(SECRET_KEY="dev", DATABASE=DB_URL)
    # https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html#basic-usage
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config["JWT_SECRET_KEY"] = "dev"  # Change this!
    jwt = JWTManager(app)

    # https://flask.palletsprojects.com/en/stable/tutorial/factory/
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
