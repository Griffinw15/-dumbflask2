from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def home():
    return "its working"