# coding: utf-8

l2p = [u'۰', u'۱', u'۲', u'۳', u'۴', u'۵', u'۶', u'۷', u'۸', u'۹']
p2l = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']


def persian_num_to_english(persian_num):
    persian_num = str(persian_num)
    place = 0
    for integer in l2p:
        persian_num = persian_num.replace(integer, p2l[place])
        place += 1
    return persian_num


def english_num_to_persian(english_num):
    english_num = str(english_num)
    place = 0
    for integer in p2l:
        english_num = english_num.replace(integer, l2p[place])
        place += 1
    return english_num


def int_to_persian_string(integer):
    result = ""
    tmp = int(integer)
    u = tmp % 1000
    tmp = tmp / 1000

    t = tmp % 1000
    tmp = tmp / 1000

    m = tmp % 1000
    b = tmp / 1000

    return result
