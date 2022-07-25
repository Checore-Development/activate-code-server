from flask import Blueprint, request, jsonify

class Application:
    def __init__(self, *args, **kwargs):
        self.server = kwargs.get('server')
        self.database = self.server.database
        self.status = self.server.status
        self.random = self.server.random
        self.app = None
        self.status = None
        self.urls = [
            ['/', self.generate_code, ['GET']]
        ]
        self.setup_app()
        self.setup_urls()
    
    def setup_app(self):  
        self.app = Blueprint('Application', __name__)

    def setup_urls(self):
        for url in self.urls:
            self.app.add_url_rule(rule=url[0], view_func=url[1], methods=url[2])
            
    def generate_code(self):
        print(request.accept_languages)
        return self.random.token()