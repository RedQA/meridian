import os
import sys
import yaml

from flask import Flask, g
from db import DB

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

db_path = custom_yaml_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "meridian.json")

# set the database instance to the app.config
app.config.project_db = DB(db_path=db_path)
