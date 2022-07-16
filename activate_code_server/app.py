from flask import Blueprint

app = Blueprint('app', __name__)

@app.route('/')
def root():
    return 'Hello World!'