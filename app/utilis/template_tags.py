from flask.ext.babel import gettext
from persian import english_num_to_persian
from date import gregorian_to_jalali, normalize_time


def tags():
    return dict(_=gettext, persian=english_num_to_persian, format=format, time=normalize_time, jalali=gregorian_to_jalali)