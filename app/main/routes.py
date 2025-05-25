import json

from flask import flash, g, redirect, render_template, request, session, url_for

from app.auth import login_required, role_required
from app.db import get_db, query_db

from . import main_bp


@main_bp.route("/")
@login_required
def home():
    # return render_template("main/home.html")
    return redirect(url_for("main.conversations"))  # redirect for now bc no dashboard


@main_bp.route("/chat/<string:id>")
@login_required
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
@login_required
def conversations():
    if session.get("role") == "admin":
        conversations = query_db("SELECT * from conversations")
    else:
        conversations = query_db(
            """
        SELECT * FROM conversations c
        JOIN conversation_members cm
        ON c.id = cm.conversation_id
        WHERE cm.user_id = ?
        """,
            [session.get("user_id")],
        )
    if not conversations:
        flash("No chats found", "info")

    return render_template("main/conversations.html", conversations=conversations)


@main_bp.route("conversations/<string:id>")
@login_required
def conversation(id):
    conv = query_db("SELECT * from conversations WHERE id = ?", [id], one=True)
    users = query_db(
        """
        SELECT cm.role,u.username, u.email FROM conversation_members cm
        JOIN users u ON u.id=cm.user_id
        WHERE conversation_id = ?
        ORDER BY cm.role desc
        """,
        [conv["id"]],
    )
    for user in users:
        print(user["username"])
    return render_template("main/conversations_id.html", conv=conv, users=users)


@main_bp.route("groups/create")
@login_required
@role_required("admin")
def create_conversation():
    if request.method == "POST":
        
        return redirect(url_for("groups"))
    else:
        users = query_db("SELECT * FROM USERS")
        return render_template("main/groups_create.html", users=users)


@main_bp.route("/users")
@role_required("admin")
@login_required
def users():
    users = query_db("SELECT * from users WHERE id != ? ", [session.get("user_id")])
    return render_template("main/users.html", users=users)


@main_bp.route("/groups")
@role_required("admin")
@login_required
def groups():
    groups = query_db("SELECT * from conversations WHERE type = 'group'")
    return render_template("main/groups.html", groups=groups)
