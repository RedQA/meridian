import json

from flask import Blueprint, current_app, jsonify, render_template, request

from apps.middleware import gd
from apps.projects.files import (get_directory_structure, is_directory,
                                 read_file_with_type)

project = Blueprint("project", __name__,
                    template_folder="../../templates", static_folder="../.../static")


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
            return "structure.html", d_content
        else:
            f_content, code_type, code_type_script = read_file_with_type(path)
            print code_type,code_type_script
            if f_content:
                f_context = {
                    "content": f_content,
                    "code_type": code_type,
                    "code_type_script": code_type_script,
                    "breadlinks": breadlinks
                }
                return "code.html", f_context
            else:
                f_context = {
                    "content": "print 'I could not load the content'",
                    "code_type": "py",
                    "code_type_script": "shBrushPython.js",
                    "breadlinks": breadlinks
                }
                return "code.html", f_context

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
