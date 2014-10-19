from functools import wraps
from flask import g, request, abort


def title(text):
    def decorator_arg(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            g.title = text
            return f(*args, **kwargs)
        return decorator
    return decorator_arg


def ajax_view(f):
    """
    Response only to ajax request other wise abort 404
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if request.headers.get('X_REQUESTED_WITH') == 'XMLHttpRequest':
            return f(*args, **kwargs)
        return abort(404)
    return decorator