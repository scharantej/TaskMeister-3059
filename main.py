
# Flask Application Generator
# Generates a simple To-Do app based on a given design

from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add-task", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect(url_for("index"))

@app.route("/remove-task", methods=["POST"])
def remove_task():
    task = request.form["task"]
    tasks.remove(task)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
