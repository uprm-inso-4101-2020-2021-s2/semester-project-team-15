from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.students import Students
from controller.tasks import Tasks

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/OfCourse/')
def home():
    return "home"


# User Management Routes

@app.route("/OfCourse/students/", methods=["GET", "POST"])
def manageStudents():
    if request.method == "GET":
        return Students().getAllStudents()
    elif request.method == "POST":
        return Students().addStudent(s_json=request.json)
    else:
        return jsonify("Method Not Allowed"), 405


@app.route("/OfCourse/students/<int:s_id>", methods=["GET", "PUT", "DELETE"])
def manageStudent(s_id):
    if request.method == "GET":
        return Students().getStudentByID(s_id)
    elif request.method == "PUT":
        return Students().updateStudentByID(s_id, request.json)
    elif request.method == "DELETE":
        return Students().deleteStudentByID(s_id)
    else:
        return jsonify("Method Not Allowed"), 405


# Course Management Routes

@app.route("/OfCourse/courses/")
def addCourse():
    return "foo"


# Task Management Routes

@app.route("/OfCourse/tasks/", methods=["GET"])
def getAllTasks():
    if request.method == "GET":
        return Tasks().getAllTasks()
    else:
        return jsonify("Method Not Allowed"), 405


@app.route("/OfCourse/tasks/<int:t_id>", methods=["GET", "PUT", "DELETE"])
def manageTasks(t_id):
    if request.method == "GET":
        return Tasks().getTaskByID(t_id)
    elif request.method == "PUT":
        return Tasks().updateTaskByID(t_id, request.json)
    elif request.method == "DELETE":
        return Tasks().deleteTaskByID(t_id)
    else:
        return jsonify("Method not Allowed"), 405


# Resource Management Routes

@app.route("/OfCourse/resources/")
def addResource():
    return "foo"


# Calendar Management Routes

app.route("/OfCourse/calendars/")


def getCalendar():
    return "foo"


if __name__ == '__main__':
    app.run(debug=True)
