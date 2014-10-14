from flask.ext.babel import gettext


def tags():
    return dict(_=gettext)