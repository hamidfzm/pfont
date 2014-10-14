from suds.client import Client as SoapClient
from lxml import objectify
#import logging
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#print(client)


class SMS(object):
    def __init__(self, app=None):
        self.sender = None
        self.soapservice = None
        self.user = None
        self.password = None

        self.template = '<xmsrequest>' + \
                        '<userid>{userid}</userid>' + \
                        '<password>{password}</password>' + \
                        '<action>smssend</action>' + '<body>' + \
                        '<type>otm</type>' + \
                        '<message originator="{sender}">{message}</message>' + \
                        '<recipient>{number}</recipient>' + \
                        '</xmsrequest>'

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Set up this instance for use with *app*, if no app was passed to
        the constructor.
        """
        self.sender = app.config['SMS_SENDER']
        self.soapservice = app.config['SMS_SOAP_SERVICE']
        self.user = app.config['SMS_USERNAME']
        self.password = app.config['SMS_PASSWORD']

    def send(self, number, message):
        client = SoapClient(self.soapservice)

        response = client.service.XmsRequest(
            self.template.format(userid=self.user,
                                 password=self.password,
                                 sender=self.sender,
                                 message=message,
                                 number=number)
        )

        try:
            response = objectify(response)
            return str(response), response.get('mobile', None)
        except:
            return 'error', response
