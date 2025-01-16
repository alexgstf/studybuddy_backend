from flask import request, jsonify, Blueprint
from model.tasksbase import db, Task

addtaskapi = Blueprint('addtaskapi', __name__)

@addtaskapi.route('/api/addtask', methods=['POST'])
def add_task():
    data = request.get_json()
    newtask = data.get('task')

    if not all([newtask]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = Task(task=newtask)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return jsonify({'message': 'Task added successfully'}), 201