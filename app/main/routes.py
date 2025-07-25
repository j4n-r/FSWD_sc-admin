import json
import os
import uuid

from flask import (
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.auth import login_required, role_required
from app.db import get_db, query_db

from . import main_bp


@main_bp.route("/")
@login_required
def home():
    return redirect(url_for("main.conversations"))


@main_bp.route("/chat/<string:id>")
@login_required
def chat(id):
    WS_URL = os.getenv("WS_URL")
    if WS_URL == None:
        WS_URL = "ws://0.0.0.0:8080"
    conv = query_db("SELECT * FROM conversations WHERE id = ?", [id], one=True)
    for row in conv:
        print(row)
    messages = query_db(
        "SELECT * FROM messages m JOIN users u ON m.sender_id==u.id WHERE conversation_id = ? ORDER BY sent_from_server",
        [conv["id"]],
    )
    return render_template(
        "main/chat_id.html",
        conv=conv,
        messages=messages,
        WS_URL=WS_URL,
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


@main_bp.route("/groups/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_conversation():
    users = query_db("SELECT id, username, role, created_at FROM users")
    form = request.form

    if request.method == "POST" and form:
        group_name = form.get("conv_name")
        description = form.get("conv_description")
        selected_member_ids = request.form.getlist("initial_members")

        group_id = str(uuid.uuid4())

        db = get_db()
        try:
            db.execute(
                """
                INSERT INTO conversations (id, owner_id, name, description) 
                VALUES (?, ?, ?, ?)
                """,
                (group_id, session.get("user_id"), group_name, description),
            )

            db.execute(
                """
                INSERT INTO conversation_members (conversation_id, user_id, role) 
                VALUES (?, ?, 'owner')
                """,
                (group_id, session.get("user_id")),
            )

            for member_id in selected_member_ids:
                if member_id != session.get("user_id"):
                    db.execute(
                        """
                        INSERT INTO conversation_members (conversation_id, user_id, role) 
                        VALUES (?, ?, 'member')
                        """,
                        (group_id, member_id),
                    )

            db.commit()
            flash("Group created successfully!", "success")
            return redirect(url_for("main.groups"))

        except Exception as e:
            db.rollback()
            flash("Error creating group. Please try again.", "error")
            print(f"Error creating group: {e}")

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
    groups = query_db("SELECT * from conversations")
    return render_template("main/groups.html", groups=groups)


@main_bp.route("/groups/delete/<string:group_id>", methods=["POST"])
@login_required
@role_required("admin")
def delete_group(group_id):
    db = get_db()
    try:
        db.execute(
            "DELETE FROM conversation_members WHERE conversation_id = ?", (group_id,)
        )
        db.execute("DELETE FROM messages WHERE conversation_id = ?", (group_id,))
        db.execute("DELETE FROM conversations WHERE id = ?", (group_id,))
        db.commit()
        flash("Group deleted successfully.", "success")
    except Exception as e:
        db.rollback()
        flash("Error deleting group.", "error")
        print(f"Error deleting group: {e}")
    return redirect(url_for("main.groups"))


@main_bp.route("/groups/<string:group_id>/edit", methods=["GET", "POST"])
@login_required
@role_required("admin")
def edit_group(group_id):
    db = get_db()
    group = query_db("SELECT * FROM conversations WHERE id = ?", [group_id], one=True)

    if not group:
        flash("Group not found", "error")
        return redirect(url_for("main.groups"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        try:
            db.execute(
                "UPDATE conversations SET name = ?, description = ? WHERE id = ?",
                (name, description, group_id),
            )
            db.commit()
            flash("Group updated successfully!", "success")
            return redirect(url_for("main.groups"))
        except Exception as e:
            db.rollback()
            flash("Error updating group", "error")
            print(e)

    return render_template("main/groups_edit.html", group=group)


# Edit user form anzeigen
@main_bp.route("/users/edit/<string:user_id>", methods=["GET"])
def edit_user(user_id):
    user = query_db("SELECT * FROM users WHERE id = ?", [user_id], one=True)
    if not user:
        flash("User not found", "error")
        return redirect(url_for("main.users"))
    return render_template("main/users_edit.html", user=user)


# Änderungen speichern
@main_bp.route("/users/edit/<string:user_id>", methods=["POST"])
def update_user(user_id):
    username = request.form.get("username")
    email = request.form.get("email")
    role = request.form.get("role")

    db = get_db()
    db.execute(
        """
        UPDATE users
        SET username = ?, email = ?, role = ?
        WHERE id = ?
    """,
        [username, email, role, user_id],
    )
    db.commit()

    flash("User updated successfully", "success")
    return redirect(url_for("main.users"))


@main_bp.route("/users/delete/<string:user_id>", methods=["POST"])
def delete_user(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", [user_id])
    db.commit()
    flash("User deleted successfully", "success")
    return redirect(url_for("main.users"))
