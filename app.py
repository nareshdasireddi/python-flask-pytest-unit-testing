from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data['title']}
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task['title'] = data['title']
    return jsonify({'task': task})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
