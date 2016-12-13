from flask import Blueprint, render_template, current_app
from apps.middleware import gateway
index = Blueprint("home", __name__, static_folder="../static",
                  template_folder="../templates")


@index.route('/')
@gateway
def home():
    return False, 'index.html', {}
