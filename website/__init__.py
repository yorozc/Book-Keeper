# Project config

from flask import Flask, render_template, redirect, request
from flask_scss import Scss
import os

app = Flask(__name__)

Scss(app)

# protects from cross-site scripting

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")

from .routes import routes
from .auth import auth

app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')