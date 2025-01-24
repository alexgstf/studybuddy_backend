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

@addtaskapi.route('/api/deletetask/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while deleting the task'}), 500

    return jsonify({'message': 'Task deleted successfully'}), 200
