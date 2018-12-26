class Adapter():

    def __init__(self, wsgi_application, responses_framework):
        self.wsgi_application = wsgi_application
        self.responses_framework = responses_framework
