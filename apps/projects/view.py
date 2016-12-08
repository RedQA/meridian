import json
from config import app

from flask import Blueprint, render_template, jsonify

project = Blueprint("project", __name__,
                    template_folder="../../templates", static_folder="../.../static")


@project.route("/")
def projects():
    return jsonify({})


@project.route("/tree/<path:fpath>")
def project_tree_path(fpath):
    pass
