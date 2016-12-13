from functools import wraps
from flask import current_app, render_template, jsonify


def gateway(view_method):
    @wraps(view_method)
    def wrapper(*args, **kwargs):
        """
            If render the template , should return 
                False, {template_name}, context
            Elif render the api , should return
                True, {is_success}, {error_message},{content}
        """
        results = view_method(*args, **kwargs)
        if results[0]:
            # json api
            is_success, error_msg, content = bool(
                results[1]), results[2], results[3]
            return jsonify({
                "is_success": is_success,
                "error_msg": error_msg,
                "content": content
            })
        else:
            # render html
            template_name = results[1]
            context = results[2]
            # template render
            projects = current_app.config.db.get_all_projects()
            context["projects"] = projects
            return render_template(template_name, **context)

    return wrapper
