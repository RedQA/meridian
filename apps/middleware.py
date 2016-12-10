from functools import wraps
from flask import current_app, render_template, jsonify


def gd(view_method):
    @wraps(view_method)
    def wrapper(*args, **kwargs):
        template, context, content = view_method(*args, **kwargs)
        if template:
            # template render
            projects = current_app.config.db.get_all_projects()
            context["projects"] = projects
            return render_template(template, **context)
        else:
            # support it's the api render
            return jsonify(content)
    return wrapper
