from flask.ext.babel import gettext
from persian import english_num_to_persian


def tags():
    return dict(_=gettext, persian=english_num_to_persian, format=format)