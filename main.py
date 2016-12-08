#!coding: utf8

from flask import render_template
from config import app

from apps.projects.views import project
from apps.views import index

app.register_blueprint(project, url_prefix="/projects")
app.register_blueprint(index)

if __name__ == "__main__":
    app.run()
