from flask import Blueprint, render_template, current_app

index = Blueprint("home", __name__, static_folder="../static",
                  template_folder="../templates")


@index.route('/')
def home():
    return render_template('index.html')
