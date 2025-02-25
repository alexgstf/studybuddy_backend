from flask import request, jsonify, Blueprint
from model.tasksbase import db, Task

addtaskapi = Blueprint('addtaskapi', __name__)

# CREATE - Add a new task
@addtaskapi.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    newtask = data.get('task')

    if not newtask:
        return jsonify({'error': 'Missing task data'}), 400

    new_task = Task(task=newtask)
    try:
        new_task.create()
        return jsonify({'message': 'Task added successfully', 'task_id': new_task.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# READ - Get all tasks
@addtaskapi.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.read() for task in tasks]), 200

# READ - Get a single task by ID
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.read()), 200

# UPDATE - Modify an existing task
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    new_task_data = data.get('task')
    if not new_task_data:
        return jsonify({'error': 'Missing task data'}), 400

    try:
        task._task = new_task_data  # Update the task field
        task.update(None)  # Call update method
        return jsonify({'message': 'Task updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE - Remove a task
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    try:
        task.delete()
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500