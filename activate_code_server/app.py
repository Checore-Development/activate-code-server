from flask import Blueprint

class Application:
    def __init__(self, *args, **kwargs):
        self.server = kwargs.get('server')
        self.database = self.server.database
        self.app = None
        self.setup_app()
        self.setup_urls()
    
    def setup_app(self):  
        self.app = Blueprint('Application', __name__)
    
    def setup_urls(self):
        urls = [
            ['/', self.generate_code, ['GET']]
        ]
        
        for url in urls:
            self.app.add_url_rule(rule=url[0], view_func=url[1], methods=url[2])
            
    def generate_code(self):
        return self.server.host