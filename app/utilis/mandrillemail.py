# -*- coding: utf-8 -*-

# python import
import mandrill


class MandrillEmail(object):
    def __init__(self, app=None):
        self.api_key = None
        self.domains = None
        self.mail = None
        self.name = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Set up this instance for use with *app*, if no app was passed to
        the constructor.
        """
        self.api_key = app.config['MANDRILL_API_KEY']
        self.domains = app.config['GOOGLE_ANALYTICS_DOMAINS']
        self.mail = app.config['NO_REPLY_MAIL_ADDRESS']
        self.name = app.config['NO_REPLY_MAIL_NAME']

    def send(self, subject, to_mail, to_name, message, async=True):
        try:
            mandrill_client = mandrill.Mandrill(self.api_key)
            message = {
                'inline_css': True,
                'html': message,
                'from_email': self.mail,
                'from_name': self.name,
                'subject': subject,
                'to': [{'email': to_mail,
                        'name': to_name,
                        'type': 'to'}],
                'google_analytics_domains': self.domains,
            }

            return mandrill_client.messages.send(message=message, async=async)

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
            # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
            raise