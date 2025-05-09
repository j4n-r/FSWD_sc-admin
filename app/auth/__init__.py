import functools

from flask import Blueprint, g, redirect, session, url_for

from app.db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        )


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


from . import routes  # noqa: E402
