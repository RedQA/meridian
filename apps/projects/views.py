import json
import os
from copy import deepcopy

from flask import Blueprint, current_app, jsonify, render_template, request,abort

from apps.covstats import get_hit_set
from apps.middleware import gd
from apps.projects.files import (get_directory_structure, is_directory,
                                 read_file_with_type)
from apps.schema import project_schema

project = Blueprint("project", __name__,
                    template_folder="../../templates", static_folder="../.../static")


@project.route("/", methods=['GET', 'POST'])
@gd
def projects_root():
    if request.method == "GET":
        projects = current_app.config.db.get_all_projects()
        return None, None, projects
    elif request.method == "POST":
        form_data = request.form
        pname = form_data["pname"]
        redisdb = int(form_data["redisdb"])
        gitaddr = form_data["gitaddr"]
        drname = form_data["drname"]
        sourcelist = form_data["sourcelist"]
        # create the new data record
        new_project_record = deepcopy(project_schema)
        new_project_record["pname"] = pname
        new_project_record["redisdb"] = redisdb
        new_project_record["gitaddr"] = gitaddr
        new_project_record["drname"] = drname
        new_project_record["sourcelist"] = sourcelist.split(",")
        new_project_record["fsroot"] = os.path.join(
            current_app.config.git_repo_root, drname)
        current_app.config.db.create_project(new_project_record)

        context = {
            "project": new_project_record
        }

        return "project_node.html", context, None


@project.route("/<string:pname>/clean/", methods=[POST'])
@gd
def clean_project_redis(pname):
    project = current_app.config.db.get_project_by_name(pname)
    if project:
        # remove the redis
    else:
        abort(404)

@project.route("/<string:pname>/tree/")
@project.route("/<string:pname>/tree/<path:fpath>")
@gd
def project_tree_path(pname, fpath=None):
    project = current_app.config.db.get_project_by_name(pname)
    if project:
        ret, path = is_directory(project, fpath)
        breadlinks = bread_link(pname, fpath)
        if ret:
            d_content = get_directory_structure(path, request.path)
            d_content["breadlinks"] = breadlinks
            return "structure.html", d_content, None
        else:
            f_content, code_type, code_type_script = read_file_with_type(path)
            if f_content:
                hl = get_hit_set(project, fpath)
                f_context = {
                    "highlights": str(hl),
                    "content": f_content,
                    "code_type": code_type,
                    "code_type_script": code_type_script,
                    "breadlinks": breadlinks
                }
                return "code.html", f_context, None
            else:
                # work round for error
                f_context = {
                    "content": "print 'I could not load the content'",
                    "code_type": "py",
                    "code_type_script": "shBrushPython.js",
                    "breadlinks": breadlinks
                }
                return "code.html", f_context, None

    # FIXME add 404 handler


def bread_link(pname, fpath):
    ret = []
    if not fpath:
        return ret

    fpath = fpath[:-1] if fpath.endswith("/") else fpath
    paths = fpath.split("/")
    links = ["/projects", pname, "tree"]
    ret.insert(0, {"name": pname, "url": "/".join(links)})
    for path in paths:
        links.append(path)
        blink = "/".join(links)
        ret.append({"name": path, "url": blink})
    return ret
