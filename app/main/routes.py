import json

from flask import g, render_template, session

from app.auth import login_required
from app.db import get_db, query_db

from . import main_bp


@main_bp.route("/")
@login_required
def hello():
    return render_template("main/home.html")


@main_bp.route("/chat/<string:id>")
def chat(id):
    conv = query_db("SELECT * FROM conversations WHERE id = ?", [id], one=True)
    for row in conv:
        print(row)
    messages = query_db(
        "SELECT * FROM messages m JOIN users u ON m.sender_id==u.id WHERE conversation_id = ? ORDER BY sent_from_server",
        [conv["id"]],
    )
    print(messages[0]["sender_id"])
    return render_template(
        "main/chat_id.html",
        conv=conv,
        messages=messages,
        user_id=session.get("user_id"),
    )


@main_bp.route("/conversations")
def conversations():
    conversations = query_db("SELECT * from conversations")
    print(conversations[0]["id"])
    return render_template("main/conversations.html", conversations=conversations)


@main_bp.route("conversations/<string:id>")
def conversation(id):
    conv = query_db("SELECT * from conversations WHERE id = ?", [id], one=True)
    users = query_db(
        """
        SELECT cm.role,u.username, u.email c FROM conversation_members cm
        JOIN users u ON u.id=cm.user_id
        WHERE conversation_id = ?
        ORDER BY cm.role desc
        """,
        [conv["id"]],
    )
    for user in users:
        print(user["username"])
    return render_template("main/conversations_id.html", conv=conv, users=users)
