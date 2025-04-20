from flask import (
    render_template,
)

from app.auth import login_required

from . import main_bp


@main_bp.route("/")
@login_required
def hello():
    return render_template("main/home.html")


@main_bp.route("/chat")
def chat():
    return render_template("main/chat.html")
