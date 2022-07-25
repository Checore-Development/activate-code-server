from flask import Flask
from gevent.pywsgi import WSGIServer

from .database import database
from .status import status_code
from .generate import generate_code

class app_server(object):
    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', 'localhost') # hostname or IP address
        self.port = kwargs.get('port', 8000) # hostport or port number
        self.database_engine = kwargs.get('database_engine', 'sqlite3') # database engine (sqlite, mysql, postgresql, mongodb)
        self.database_filename = kwargs.get('database_filename', 'database') # database filename (only for sqlite)
        self.database_host = kwargs.get('database_host', '127.0.0.1') # database host (localhost, 127.0.0.1)
        self.database_port = kwargs.get('database_port') # database port (3306, 5432, 27017)
        self.database_name = kwargs.get('database_name', 'activate_code_server') # database name
        self.database_user = kwargs.get('database_user', 'root') # database user (root)
        self.database_password = kwargs.get('database_password', '12345678') # database password
        self.code_format = kwargs.get('code_format', 'xxxxx-xxxxx-xxxxx-xxxxx-xxxxx') # code format
        self.encrypted = kwargs.get('encrypted', 'False') # encrypted method 
        self.app = None # flask app
        self.server = None # flask server
        self.database = None # database
        self.status = None # status code
        self.generate = None # generate
        self.setup_app() # setup flask app
        self.setup_database() # setup database
        self.setup_status() # setup status_code application
        self.setup_generate() # setup generate_code application

    def setup_app(self):
        self.app = Flask(__name__)
    
    def setup_blueprint(self, blueprint):
        applications = blueprint(server=self)
        self.app.register_blueprint(applications.app)

    def setup_server(self):
        self.server = WSGIServer(
            (self.host, self.port),
            self.app)
    
    def setup_database(self):
        db = database(
            database_engine=self.database_engine,
            database_filename=self.database_filename,
            database_host=self.database_host,
            database_port=self.database_port,
            database_name=self.database_name,
            database_user=self.database_user,
            database_password=self.database_password
        )
        self.database = db.database
    
    def setup_status(self):
        self.status = status_code()
    
    def setup_generate(self):
        self.generate = generate_code(
            code_format=self.code_format
        )
    
    def run(self):
        self.setup_server()
        self.server.serve_forever()