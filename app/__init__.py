from flask import Flask
# from flask.ext.bootstrap import Bootstrap
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

from app.utilis.sms import SMS
from config import config


# bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
babel = Babel()
db = MongoEngine()
sms = SMS()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    babel.init_app(app)
    sms.init_app(app)

    app.session_interface = MongoEngineSessionInterface(db)

    # Registering blue prints
    from main import mod
    # from auth import auth
    # from user import user

    app.register_blueprint(mod)
    # app.register_blueprint(auth)
    # app.register_blueprint(user)

    # Registering custom template tags
    from app.utilis.template_tags import tags

    # from app.auth.models import User, GuestUser

    app.template_folder = '../templates'
    app.static_folder = '../statics'
    # app.host = config['HOST']
    #app.port = config['PORT']

    # @app.before_request
    # def before_request():
    #     """
    #     """
    #     if 'logged_in' in session:
    #         try:
    #             g.user = User.objects.get(pk=session.get('logged_in'))
    #         except DoesNotExist:
    #             g.user = GuestUser()
    #     else:
    #         g.user = GuestUser()

    app.context_processor(tags)

    # attach routes and custom error pages here
    return app