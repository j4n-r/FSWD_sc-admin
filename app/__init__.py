import os

from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="aacda941c9732a27083a3df451ab86d8d1d87f9085567fc93528172db61a8c9e",
        DATABASE=os.path.join(app.instance_path, "dev.sqlite3"),
    )
    from . import db

    db.init_app(app)

    # a simple page that says hello
    @app.route("/")
    def hello():
        return render_template("home.html")

    return app
