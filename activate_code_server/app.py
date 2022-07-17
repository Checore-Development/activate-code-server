from flask import Blueprint

__all__ = ["app"]

app = Blueprint('app', __name__)

@app.route('/')
def root():
    return 'Hello World!'