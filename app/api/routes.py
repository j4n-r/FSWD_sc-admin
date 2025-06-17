from flask_jwt_extended import get_jwt_identity, jwt_required

from app.db import query_db

from . import api_bp


@api_bp.route("/user/<string:user_id>/conversations")
# @jwt_required(refresh=True)
def conversation(user_id):
    """
    Get all conversations for a user.
    """
    conversations = query_db(
        """
            SELECT * FROM conversations c
            JOIN conversation_members cm ON c.id = cm.conversation_id
            WHERE cm.user_id = ?
            """,
        [user_id],
    )

    if not conversations:
        return {"message": "No conversations found"}, 404

    return {"conversations": [dict(conv) for conv in conversations]}, 200
