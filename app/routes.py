import datetime
from flask import jsonify, request
# This imports the Task class and db object defined in models.py
from app.models import Task, db
# This imports the app object defined in app/__init__.py
from app import app

# 2.1 Create Task API
@app.route('/task', methods=['POST'])
def add_task():
    # Check for valid input data
    name = request.json['name']
    category = request.json['category']
    if category not in ['Work', 'Personal', 'School', 'Others']:
        return jsonify({'message': 'Invalid category'}), 400
    dueDate = datetime.datetime.strptime(request.json['dueDate'], '%Y-%m-%d')
    if not (name and dueDate):
        return jsonify({'message': 'Name or Due Date cannot be null'}), 400
    existing_task = Task.query.filter_by(name=name).first()
    if existing_task is not None:
        return jsonify({'message': 'Task already exists'}), 400
    else:
        # Create a new Task object with the provided data.
        new_task = Task(name=name, category=category, dueDate=dueDate)
        # Add the new task to the database
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id, 'name': new_task.name, 'category': new_task.category, 'dueDate': new_task.dueDate.strftime('%Y-%m-%d')})

# 2.2 Update Task API
@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    name = request.json['name']
    category = request.json['category']
    # Check for valid input data
    if category not in ['Work', 'Personal', 'School', 'Others']:
        return jsonify({'message': 'Invalid category'}), 400
    dueDate = datetime.datetime.strptime(request.json['dueDate'], '%Y-%m-%d')
    if not (name and dueDate):
        return jsonify({'message': 'Name or dueDate cannot be null'}), 400
    # Update the task attributes with the new values
    task.name = name
    task.category = category
    task.dueDate = dueDate
    db.session.commit()
    return jsonify({'id': task.id, 'name': task.name, 'category': task.category, 'dueDate': task.dueDate.strftime('%Y-%m-%d')})    

# 2.3 Delete Task API
@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    # Delete the task from the database.
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})

# 2.4 Retrieve Tasks API
@app.route('/task', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = [{'id': task.id, 'name': task.name, 'category': task.category,
               'dueDate': task.dueDate.strftime('%Y-%m-%d')} for task in all_tasks]
    return jsonify(result)
