from functools import wraps
from flask import g


def title(text):
    def decorator_arg(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            g.title = text
            return f(*args, **kwargs)
        return decorator
    return decorator_arg