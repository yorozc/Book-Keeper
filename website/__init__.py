# Project config

from flask import Flask, render_template, redirect, request
from flask_scss import Scss

app = Flask(__name__)

Scss(app)

# protects from cross-site scripting

app.config["SECRET_KEY"] = "4bb18d83f092ecdbfcb9a027b7ca4077e744c79e"

from .routes import routes
from .auth import auth

app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')