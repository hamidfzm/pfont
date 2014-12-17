from datetime import date
from app.libs.calverter import Calverter


def jalali_to_gregorian(date_str):
    if not date_str:
        return ''
    if date_str == "":
        return ""
    cal = Calverter()
    year, month, day = date_str.split("/")
    jd = cal.jalali_to_jd(int(year), int(month), int(day))
    gre = cal.jd_to_gregorian(jd)
    return date(gre[0], gre[1], gre[2])


def gregorian_to_jalali(date):
    if not date:
        return ''
    if isinstance(date, str):
        date = parser(date)
    if isinstance(date, unicode):
        date = parser(date)
    cal = Calverter()
    jd = cal.gregorian_to_jd(date.year, date.month, date.day)
    jalali = cal.jd_to_jalali(jd)
    return "%s/%s/%s" % (jalali[0], jalali[1], jalali[2])


def parser(date_str):
    try:
        year, month, day = date_str.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        return 0, 0, 0


def normalize_date(date_obj):
    if isinstance(date_obj, date):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return date_obj


def normalize_time(date_obj):
    if isinstance(date_obj, date):
        return date_obj.strftime('%H:%M')
    else:
        return date_obj