from shotgun_api3 import Shotgun
import pprint
import requests

key = 'osayi0frbwuqiSizj#tiatdyz'
script_name = "connect_api"

sg = Shotgun("https://sagar.shotgrid.autodesk.com", "readAccess", key)


class ShortGird:
    def __init__(self):
        self.sg = Shotgun("https://sagar.shotgrid.autodesk.com", "readAccess", key)

    def get_projects(self):
        # proj_list = sg.find("Project", [['sg_status','is','']],[ 'id', 'name', 'is_demo'])
        # proj_list = sg.find("Project", [['sg_status','is','Active']],[ 'id', 'name', 'is_demo'])
        proj_list = self.sg.find("Project", [['is_demo', 'is', True]], ['id', 'name'])
        pprint.pprint(proj_list)
        return proj_list

    def get_all_shots_in_project(self, project_id):

        filters = [
            ['project.Project.id', 'is', project_id]
        ]
        fields = ['code', 'sg_sequence', 'sg_cut_in', 'sg_cut_out', 'sg_cut_duration']

        shots_list = sg.find("Shot", filters, fields)
        pprint.pprint(shots_list)
        return shots_list

    def get_project_by_id(self, project_id):
        project = sg.find("Project", [['id','is', project_id]], ['name'])
        return project

    def get_shot_by_id(self, shot_id):
        shot = sg.find("Shot", [['id','is', shot_id]], ['code'])
        return shot

    def get_tasks_in_shot(self, shot_id, fields):
        filters = [

            ['entity', 'is', {'type': 'Shot', 'id': shot_id}]

        ]

        shot_details = sg.find("Task", filters, fields)
        pprint.pprint(shot_details)
        return shot_details

