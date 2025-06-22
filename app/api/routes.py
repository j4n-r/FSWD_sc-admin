from flask import current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.db import query_db

from . import api_bp


@api_bp.route("/user/<string:user_id>/conversations")
@jwt_required()
def getUserConversations(user_id: str):
    """
    Get all conversations for a user.
    """
    current_app.logger.debug(request)
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


@api_bp.route("/conversation/<string:conv_id>/messages")
@jwt_required()
def getMessages(conv_id: str):
    """
    Get all conversations for a user.
    """
    current_app.logger.debug(request)
    conversations = query_db(
        """
            SELECT * FROM messages
            WHERE conversation_id = ?
            """,
        [conv_id],
    )

    if not conversations:
        return {"message": "No conversations found"}, 404

    return {"messages": [dict(conv) for conv in conversations]}, 200


@api_bp.route("/conversation/<string:conv_id>")
@jwt_required()
def getConversation(conv_id: str):
    """
    Get all conversations for a user.
    """
    current_app.logger.debug(request)
    conversation = query_db(
        """
            SELECT * FROM conversations
            WHERE id = ?
            """,
        [conv_id],
        True,
    )

    if not conversation:
        return {"message": "Conversation not found"}, 404

    return {"messages": dict(conversation)}, 200
