import os
import sys
import yaml

from flask import Flask, redirect
from db import JsonDB

app = Flask(__name__)
app.debug = True

custom_yaml_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "conf", "custom.yaml")

if not os.path.exists(custom_yaml_path):
    sys.stderr.write("conf/custom.yaml not existed\n")
    sys.exit(-1)

with open(custom_yaml_path, "r") as f:
    custom_config = yaml.load(f)
    git_repo_root = str(custom_config["git_repo_root"])
    if not os.path.exists(git_repo_root):
        sys.stderr.write(
            "git_repo_root=%s not existed on the filesystem" % git_repo_rootf)
        sys.exit(-1)

    app.config.git_repo_root = git_repo_root
    # redis configuration
    app.config.redis_config = custom_config["redis"]

db_path = custom_yaml_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "meridian.json")

# set the database instance to the app.config
app.config.db = JsonDB(db_path=db_path)


@app.errorhandler(404)
def page_not_found(e):
    # if 404, redirect back to the home page
    return redirect("/")
