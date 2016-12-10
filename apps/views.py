from flask import Blueprint, render_template, current_app
from apps.middleware import gd
index = Blueprint("home", __name__, static_folder="../static",
                  template_folder="../templates")


@index.route('/')
@gd
def home():
    return 'index.html', {}, None
