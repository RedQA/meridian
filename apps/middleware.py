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


def api(view_method):
    @wraps(view_method)
    def wrapper(*args, **kwargs):
        is_success, error_msg, content = view_method(*args, **kwargs)

        res = dict()
        res['is_success'] = is_success

        if error_msg is not None:
            res['error_msg'] = error_msg
        if content is not None:
            res['content'] = content

        return jsonify(res)

    return wrapper
