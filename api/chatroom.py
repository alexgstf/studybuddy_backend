from flask import Blueprint, request, jsonify

chatroom_api = Blueprint('chatroom_api', __name__)

chat_messages = []  # Temporary storage for messages

@chatroom_api.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'username' not in data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    chat_messages.append({'username': data['username'], 'message': data['message']})
    return jsonify({"success": True})

@chatroom_api.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(chat_messages)
