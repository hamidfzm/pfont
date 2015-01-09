# import python
from htmlmin.main import minify

# import flask
from flask import Flask, request, render_template
from flask.ext.babel import Babel
from flask.ext.moment import Moment
from flask.ext.mongoengine import MongoEngine

# import project
from app.utilis.mandrillemail import MandrillEmail
from config import config


moment = Moment()
babel = Babel()
db = MongoEngine()
mandrillemail = MandrillEmail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.template_folder = '../templates'
    app.static_folder = '../static'

    # bootstrap.init_app(app)
    # mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    babel.init_app(app)
    # sms.init_app(app)
    mandrillemail.init_app(app)

    # app.session_interface = MongoEngineSessionInterface(db)

    # Registering blue prints

    for blueprint in app.config['INSTALLED_BLUEPRINTS']:
            bp = __import__('app.%s' % blueprint, fromlist=[blueprint])
            app.register_blueprint(bp.mod)

    # Registering custom template tags
    from app.utilis.template_tags import tags
    app.context_processor(tags)

    # @app.before_request
    # def user_in_g():
    #     """
    #     """
    #     if 'logged_in' in session:
    #         try:
    #             g.user = User.objects.get(pk=session.get('logged_in'))
    #         except DoesNotExist:
    #             g.user = GuestUser()
    #     else:
    #         g.user = GuestUser()

    def excluld_domains():
        url = request.url_root.replace('http://', '').replace('/', '').replace('www.', '')
        if url in app.config['EXCLUDED_DOMAINS']:
            return render_template('construction.html')

    if app.config['UNDER_CONSTRUCTION']:
        app.before_request(excluld_domains)

    def response_minify(response):
            """
            minify response html to decrease traffic
            """
            if response.content_type == u'text/html; charset=utf-8':
                response.set_data(
                    minify(response.get_data(as_text=True),
                           remove_comments=True,
                           remove_empty_space=True,
                           remove_all_empty_space=True)
                )

                return response
            return response

    if app.config['MINIFY_PAGE']:
        app.after_request(response_minify)

    # blueprint with error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return '404 - Page Not Found', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return '500 - Internal Server Error', 500

    # attach routes and custom error pages here
    return app