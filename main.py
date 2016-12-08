#!coding: utf8

from flask import render_template
from config import app

from apps.projects.view import project

app.register_blueprint(project, url_prefix="/projects")


@app.route('/')
def index(name=None):
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
