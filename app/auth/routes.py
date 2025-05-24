import uuid

from flask import (
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_cors import cross_origin
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db, query_db

from . import auth_bp


@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        db = get_db()
        error = None

        if not email:
            error = "Email is required."
            current_app.logger.warn(error)
        elif not password:
            error = "Password is required."
            current_app.logger.warn(error)
        if error is None:
            try:
                query_db(
                    "INSERT INTO users (id,email,username, password) VALUES (?,?,?, ?)",
                    (
                        str(uuid.uuid4()),
                        email,
                        username,
                        generate_password_hash(password),
                    ),
                )
            except Exception as e:
                current_app.logger.warn(e)
                error = "Something went wrong"
            else:
                flash("Succesfully registered new account, please login", "register_success")
                return redirect(url_for("auth.login"))

        flash(error, "register_error")

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        error = None
        user = query_db("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if user is None:
            error = "Incorrect email."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            current_app.logger.info("%s logged in", user["email"])
            return redirect("/")

        current_app.logger.warn("%s", error)
        flash(error)

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/auth/login")


@cross_origin()
@auth_bp.route("/token", methods=("GET", "POST", "OPTIONS"))
def token():
    if request.method == "OPTIONS":
        return "", 200

    request_data = request.get_json()
    db = get_db()
    error = None
    email = None
    password = None
    if request_data:
        if "email" in request_data:
            email = request_data["email"]

        if "password" in request_data:
            password = request_data["password"]

    if not email:
        error = "Email is required."
    if not password:
        error = "Password is required."

    if error is None:
        try:
            db.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {email} is already registered."
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    user = query_db("SELECT * FROM users WHERE email=?", [email], one=True)
    if user is None:
        current_app.logger.exception("user not found in db")
        return jsonify("Something went wrong")

    additional_claims = {"user_id": user["id"], "username": user["username"]}

    access_token = create_access_token(
        email, additional_claims=additional_claims, fresh=True
    )
    refresh_token = create_refresh_token(identity=email)

    # automatically sets right headers (json.dump) only does  json
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)
