from flask import Blueprint, render_template, request, flash, jsonify
from website.functions import ShortGird

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/projects')
def home():
    sg = ShortGird()
    projects = sg.get_projects()
    return render_template("home.html", projects=projects)


@views.route('/project/<project_id>')
def get_project_shots(project_id):
    sg = ShortGird()
    project = sg.get_project_by_id(int(project_id))
    data = {'name': project[0]["name"]}
    data["shots"] = shots = sg.get_all_shots_in_project(int(project_id))
    return render_template("project_details.html", data=data)


@views.route('/shot/<shot_id>')
def get_shot_details(shot_id):
    sg = ShortGird()
    shot = sg.get_shot_by_id(int(shot_id))
    data = {'name': shot[0]["code"]}
    data["tasks"] = sg.get_tasks_in_shot(int(shot_id), ['content', 'step', 'assigned_to', 'start_date', 'due_date', 'duration', 'bid'])
    return render_template("shot_details.html", data=data)
