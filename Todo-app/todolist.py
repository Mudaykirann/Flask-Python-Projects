from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def home():
    return render_template('todo.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    if todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
