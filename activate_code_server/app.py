from flask import Blueprint, request, jsonify

class Application:
    def __init__(self, *args, **kwargs):
        self.server = kwargs.get('server')
        self.database = self.server.database
        self.app = None
        self.urls = [
            ['/', self.generate_code, ['GET']]
        ]
        self.status = None
        self.setup_app()
        self.setup_urls()
        self.setup_status()
    
    def setup_app(self):  
        self.app = Blueprint('Application', __name__)
    
    def setup_status(self):
        self.status = self.server.status
        
    def setup_urls(self):
        for url in self.urls:
            self.app.add_url_rule(rule=url[0], view_func=url[1], methods=url[2])
            
    def generate_code(self):
        pass