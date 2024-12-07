from flask import Blueprint, jsonify, request

from client_mood_track_api.utils import CommentProcessor, TwilioHandler

v1_blueprint = Blueprint("v1", __name__)


@v1_blueprint.route("/comment-analysis", methods=["POST"])
def analyze_comment_v1():
    print("Start...")
    data = request.get_json()
    processor = CommentProcessor(data)
    twilio = TwilioHandler()
    status = processor.process_comment()
    user_name = data.get("userName")

    if status:
        twilio.send_confirmation_message(data)
        print("End...")
        return jsonify({"message": f"{user_name} comment processed!"}), 200
    else:
        print("End...")
        return jsonify({"message": f"Error processing {user_name}`s comment!"}), 400


# POST /comment-analysis - Classifies a single comment using ChatGPT
# GET /comments Retrieves all classified comments.
# GET /comments/{id} Retrieves a single classified comment by its ID.
# DELETE /comments/{id}  Deletes a classified comment by its ID.
# PUT /comments/{id} Updates a previously classified comment by its ID.
