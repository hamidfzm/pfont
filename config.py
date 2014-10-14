import os

# from flask.ext.babel import gettext as _

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = "_<TCDJ p|fqcj>f%LyLKqmZj57+G-DlC-U^<+C(+rIy_6|nCHn^#zYWoT= 9=j"
    WTF_CSRF_SECRET_KEY = "0E9B059ED83BCA5F90F1814F2AE014553D4A3F4E3C05F42B178869C879749A29"

    # RECAPTCHA_PUBLIC_KEY = "6LfJT_gSAAAAAHUcp-NtDYguqZGe4kAyqGptNK7q"
    # RECAPTCHA_PRIVATE_KEY = "6LfJT_gSAAAAABL_zPayoW_6uAn-3ZXh9Pf8zHgQ"
    # RECAPTCHA_OPTIONS = {
    #     'theme': 'custom',
    #     'custom_theme_widget': 'recaptcha_widget',
    #     'custom_translations': {
    #         'visual_challenge': _('Get a visual challenge'),
    #         'audio_challenge': _('Get an audio challenge'),
    #         'refresh_btn': _('Get a new challenge'),
    #         'instructions_visual': _('Type the two words:'),
    #         'instructions_audio': _('Type what you hear:'),
    #         'help_btn': _('Help'),
    #         'play_again': _('Play sound again'),
    #         'cant_hear_this': _('Download sound as MP3'),
    #         'incorrect_try_again': _('Incorrect. Try again.'),
    #     }
    # }
    # some nasty recaptach bebel bug fixes

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Hamid FzM]'
    FLASKY_MAIL_SENDER = 'Hamid FzM <mail@hamidfzm.ir>'
    FLASKY_ADMIN = 'Hamid FzM'
    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'UTC+03:30'

    # SMS Configs
    SMS_SENDER = '50002010060975'
    SMS_USERNAME = '6623'
    SMS_PASSWORD = 'umdxatjnlldg'
    SMS_SOAP_SERVICE = 'http://panel.bizna.ir/webservice/soap/xml.php?wsdl'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MONGODB_SETTINGS = {'DB': 'pfont',
                        'HOST': '127.0.0.1',
                        'PORT': 27017}


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {'DB': 'pfont',
                        # TODO set username and password for mongo learnhub database
                        # 'USERNAME': 'my_user_name',
                        # 'PASSWORD': 'my_secret_password',
                        'HOST': '127.0.0.1',
                        'PORT': 27017}


config = {'development': DevelopmentConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}