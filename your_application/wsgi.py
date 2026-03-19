from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    """
    Returns a greeting message for the root URL.
    """
    return 'Hello from Jules! The deployment was successful.'

