import sqlite3
from datetime import datetime

import click
from flask import current_app, g
from werkzeug.security import check_password_hash, generate_password_hash

# https://flask.palletsprojects.com/en/stable/tutorial/database/


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Run schema.sql"""
    try:
        db = get_db()

        try:
            with current_app.open_resource("init.sql") as f:
                db.executescript(f.read().decode("utf8"))
        except Exception as e:
            print(e)
        add_default_users()
        return "Initialized DB"
    except Exception:
        raise Exception


@click.command("init-db")
def init_db_command():
    """Register command `flask init-db`"""
    res = init_db()
    click.echo(res)


def drop_db():
    """Run drop.sql"""
    try:
        db = get_db()

        try:
            with current_app.open_resource("drop.sql") as f:
                db.executescript(f.read().decode("utf8"))
        except Exception as e:
            print(e)
        add_default_users()
        return "Dropped DB"
    except Exception:
        raise Exception


@click.command("drop-db")
def drop_db_command():
    """Register command `flask drop-db`"""
    res = drop_db()
    click.echo(res)


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)  # unixtimestamps


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)


def add_default_users():
    users = [
        {
            "id": "624f76c7-7b46-4309-8207-126317477e88",
            "email": "admin@admin.com",
            "username": "admin",
            "password": "admin",
            "role": "admin",
            "name": "admin",
        },
        {
            "id": "203170c2-e811-44ba-a24f-a1e57d53b363",
            "email": "test@test.com",
            "username": "test",
            "password": "test",
            "role": "user",
            "name": "test",
        },
    ]
    db = get_db()

    for user in users:
        try:
            query_db(
                """
                INSERT INTO users (id, email, username,role, password, name)
                VALUES (?, ?, ?, ?, ?,?)
                """,
                (
                    user["id"],
                    user["email"],
                    user["username"],
                    user["role"],
                    generate_password_hash(user["password"]),
                    user["name"],
                ),
            )
            print(f"Default user {user['email']} created.")
        except Exception as e:
            error = f"User {user['email']} is already registered."
            print(e)


# https://flask.palletsprojects.com/en/stable/patterns/sqlite3/#easy-querying
def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
