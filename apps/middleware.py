from flask import current_app, render_template


def gd(view_method):
    def wrapper(*args, **kwargs):
        projects = current_app.config.db.get_all_projects()
        template, context = view_method(*args, **kwargs)
        context["projects"] = projects
        return render_template(template, **context)
    return wrapper
