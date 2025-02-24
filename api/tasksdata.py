from flask import request, jsonify, Blueprint
from model.tasksbase import db, Task
from model.user import User  # Import the User model to verify user authenticity

addtaskapi = Blueprint('addtaskapi', __name__)

# CREATE - Add a new task for a specific user
@addtaskapi.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    newtask = data.get('task')
    user_id = data.get('user_id')  # Get the user_id from the request
    
    if not newtask:
        return jsonify({'error': 'Missing task data'}), 400
    
    if not user_id:
        return jsonify({'error': 'Missing user ID'}), 400

    user = User.query.get(user_id)  # Verify that the user exists
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    new_task = Task(task=newtask, _user_id=user_id)  # Associate task with user_id
    try:
        new_task.create()
        return jsonify({'message': 'Task added successfully', 'task_id': new_task.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# READ - Get all tasks for the logged-in user
@addtaskapi.route('/api/tasks', methods=['GET'])
def get_tasks():
    user_id = request.args.get('user_id')  # Assume user_id is passed as a query parameter for simplicity
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    tasks = Task.query.filter_by(_user_id=user.id).all()  # Only fetch tasks belonging to the user
    return jsonify([task.read() for task in tasks]), 200

# READ - Get a single task by ID for a specific user
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    user_id = request.args.get('user_id')  # User ID from query params
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    task = Task.query.filter_by(id=task_id, _user_id=user_id).first()  # Ensure task belongs to the user
    if not task:
        return jsonify({'error': 'Task not found or not accessible by this user'}), 404
    return jsonify(task.read()), 200

# UPDATE - Modify an existing task for a specific user
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    user_id = data.get('user_id')  # Get user ID from the request

    if not user_id:
        return jsonify({'error': 'Missing user ID'}), 400

    task = Task.query.filter_by(id=task_id, _user_id=user_id).first()  # Ensure task belongs to the user
    if not task:
        return jsonify({'error': 'Task not found or not accessible by this user'}), 404

    new_task_data = data.get('task')
    if not new_task_data:
        return jsonify({'error': 'Missing task data'}), 400

    try:
        task._task = new_task_data  # Update the task
        task.update(None)  # Update the task in the database
        return jsonify({'message': 'Task updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE - Remove a task for a specific user
@addtaskapi.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    user_id = request.args.get('user_id')  # Get user ID from query params
    
    if not user_id:
        return jsonify({'error': 'Missing user ID'}), 400

    task = Task.query.filter_by(id=task_id, _user_id=user_id).first()  # Ensure task belongs to the user
    if not task:
        return jsonify({'error': 'Task not found or not accessible by this user'}), 404

    try:
        task.delete()  # Delete the task
        return jsonify({'message': 'Task deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
