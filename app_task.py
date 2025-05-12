from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库（全局变量）
tasks = []
task_id_counter = 1

# 创建任务：POST /tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        'id': task_id_counter,
        'title': title,
        'done': False
    }
    tasks.append(new_task)
    task_id_counter += 1

    return jsonify(new_task), 201

# 获取所有任务：GET /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# 获取单个任务：GET /tasks/<id>
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

# 更新任务：PUT /tasks/<id>
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    if 'title' in data:
        task['title'] = data['title']
    if 'done' in data:
        task['done'] = data['done']

    return jsonify(task)

# 删除任务：DELETE /tasks/<id>
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': f'Task {task_id} deleted successfully'})

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
