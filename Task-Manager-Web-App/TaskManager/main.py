from flask import Flask, render_template, request, redirect, url_for
import db
from models import Task

# Our Flask web server is located in app
app = Flask(__name__)


# Slash is used for the homepage
@app.route('/')
def home():
    all_tasks = db.session.query(Task).all()  # Check and store all tasks in the database
    return render_template("index.html", list_of_tasks=all_tasks)


@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['content_task'], done=False)
    db.session.add(task)  # adding object task to database
    db.session.commit()  # execute the pending database operation
    return redirect(url_for('home'))  # Taking us back to home() function


@app.route('/task-done/<id>')
def done(id):
    task = db.session.query(Task).filter_by(id=int(id)).first()  # Gets the task you are looking for
    task.done = not task.done  # Save its opposite in teh Boolean variable of the task
    db.session.commit()  # Execute the pending database operation
    return redirect(url_for('home'))  # Takes us back to home() after completing done


@app.route('/delete-task/<id>')
def delete(id):
    task = db.session.query(Task).filter_by(id=int(id)).delete()  # Search matching id in the database provided by
    # route parameter. When it is found then it is deleted.
    db.session.commit()  # Execute the pending database operation
    return redirect(url_for('home'))  # Takes us back to home() and deleted task will be removed.


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
