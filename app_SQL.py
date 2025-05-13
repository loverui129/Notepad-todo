from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template,redirect
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # 本地数据库文件 task.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up the database connection
db = SQLAlchemy(app)

# Define the Task model (represents a table in the database)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(10), default='Low')
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    

# Automatically create the database and table
with app.app_context():
    db.create_all()

# Create task：POST /tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')

    if not title or not isinstance(title, str):
        return jsonify({'error': 'Title is required and must be a string'}), 400

    task = Task(title=title)
    db.session.add(task)
    db.session.commit()

    return jsonify({'id': task.id, 'title': task.title, 'done': task.done}), 201

# Retrieve all tasks：GET /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    results = []

    for task in tasks:
        results.append({
            'id': task.id,
            'title': task.title,
            'done': task.done
        })

    return jsonify(results)

# Get single Task：GET /tasks/<id>
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)  # find tasks
    if not task:
        return jsonify({'error': 'Task not found'}), 404


    return jsonify({
        'id': task.id,
        'title': task.title,
        'done': task.done
    })
# Update a Task with a specific ID：PUT /tasks/<id>
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    # Parse JSON input
    data = request.get_json()

    # Update fields if provided
    if 'title' in data:
        task.title = data['title']
    if 'done' in data:
        task.done = data['done']

    db.session.commit()

    return jsonify({
        'id': task.id,
        'title': task.title,
        'done': task.done
    })

# Priority function
@app.route('/update_priority/<int:task_id>, methods=[POST]')
def update_priority(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    new_priority = request.form.get('priority')
    if new_priority not in ['High','Medium','Low']:
        return jsonify({'error': 'Task not found'}), 400
    
    task.priortiy = new_priority
    db.session.commit()
    return redirect('/') 


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        priority = request.form.get('priority')
        if title:
            new_task = Task(title=title, priority=priority)
            db.session.add(new_task)
            db.session.commit()
        return redirect('/')  # After POST, redirect to home page
    
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)



# Toggle swift Button
@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}),404
    task.done = not task.done 
    db.session.commit()
    return redirect('/')

# Add delete icon for deleting tasks if finished 
@app.route('/delete/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}),404
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


# Start the Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
