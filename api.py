import flask
from flask import request, jsonify, render_template
import data

app = flask.Flask(__name__, template_folder="webroot", static_folder="webroot")
app.config["DEBUG"] = True

documentation_v1 = {}

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/api-v1', methods=['GET'])
def docs():
    return render_template("html/api-v1.html")

@app.route('/rawdocs', methods=['GET'])
def rawdocs():
    return documentation_v1

documentation_v1["/api/v1/tasks-today"] = "Returns todays scehduled tasks"
@app.route('/api/v1/tasks-today', methods=['GET'])
def api_all():
    return jsonify(data.getbooks())

documentation_v1["/api/v1/tasks-future/{count}"] = "Returns the specified number of tasks for the future"
@app.route('/api/v1/tasks-future', methods=['GET'])
def api_tasks_count():
    if 'count' in request.args:
        count = int(request.args['count'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for book in data.getbooks():
        if book['id'] == id:
            results.append(book)

    return jsonify(results)
app.run()
