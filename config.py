# -*- coding: utf-8 -*-

# python import
import os
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    CAMPAIGN_START = datetime(2014, 12, 15, 0, 0)

    SECRET_KEY = os.environ.get('SECRET_KEY_PFONT', 'Development')
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY_PFONT', 'WTFDeveloper')
    MMERCHANT_ID = os.environ.get('MMERCHANT_ID_PFONT')
    ZARINPAL_WEBSERVICE = 'https://de.zarinpal.com/pg/services/WebGate/wsdl'

    # mandrill config
    MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY_PFONT')  # use to send mail using mandrill service
    NO_REPLY_MAIL_ADDRESS = 'noreply@pfont.ir'
    NO_REPLY_MAIL_NAME = 'کمپین قلم فارسی آزاد'
    GOOGLE_ANALYTICS_DOMAINS = ['librefont.ir', 'www.librefont.ir', 'pfont.ir', 'www.pfont.ir']
    EXCLUDED_DOMAINS = ['librefont.ir', 'pfont.ir']  # if site where under construction these domains will be excluded

    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Hamid FzM]'
    FLASKY_MAIL_SENDER = 'Hamid FzM <mail@hamidfzm.ir>'
    FLASKY_ADMIN = 'Hamid FzM'

    LANGUAGES = {
        'en': 'English',
        'fa': u'فارسی'
    }

    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'UTC+03:30'

    SITE_TITLE = u'کمپین قلم فارسی آزاد'

    MONGODB_SETTINGS = {'DB': 'pfont',
                    'HOST': '127.0.0.1',
                    'PORT': 27017}

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MINIFY_PAGE = False
    UNDER_CONSTRUCTION = False


class ProductionConfig(Config):
    DEBUG = False
    MINIFY_PAGE = True

    UNDER_CONSTRUCTION = False


config = {'development': DevelopmentConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}