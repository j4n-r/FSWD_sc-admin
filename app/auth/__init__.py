import functools

from flask import Blueprint, flash, g, redirect, session, url_for

from app.db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")


# https://flask.palletsprojects.com/en/stable/tutorial/views/#id5
@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        )


# https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/#login-required-decorator
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


# this was written by an llm but I cannot find the chat anymore
# Prompt: write me this as a custom decorator https://flask-user.readthedocs.io/en/latest/authorization.html#roles-required
def role_required(role):
    def decorator(view):
        @functools.wraps(view)
        def wrapped_view(*args, **kwargs):
            if session.get("role") != role:
                flash("You do not have the needed permissons for this route", "error")
                return redirect(url_for("main.home"))
            return view(*args, **kwargs)

        return wrapped_view

    return decorator


from . import routes  # noqa: E402
