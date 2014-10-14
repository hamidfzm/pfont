from flask import render_template
from . import mod


# blueprint with error handlers
@mod.app_errorhandler(404)
def page_not_found(e):
    return '404 - Page Not Found', 404


@mod.app_errorhandler(500)
def internal_server_error(e):
    return '500 - Internal Server Error', 500