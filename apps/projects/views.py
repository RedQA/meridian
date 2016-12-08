import json
from apps.projects.files import is_directory, get_directory_structure

from flask import Blueprint, current_app, jsonify, render_template, request, current_app

project = Blueprint("project", __name__,
                    template_folder="../../templates", static_folder="../.../static")


@project.route("/")
def projects():
    if request.method == "GET":
        return jsonify({})
    elif request.method == "POST":
        pass


@project.route("/<string:pname>/tree/")
@project.route("/<string:pname>/tree/<path:fpath>")
def project_tree_path(pname, fpath=None):
    project = current_app.config.project_db.get_project_by_name(pname)
    if project:
        ret, path = is_directory(project, fpath)
        if ret:
            d_content = get_directory_structure(path, request.path)
            return render_template("structure.html", **d_content)
        else:
            return render_template("code.html",**{
                "code_type_script": "adfdsf"
            })
    # FIXME add 404 handler
