from website import app
from .db import users
from flask import render_template, request, redirect, Blueprint

routes = Blueprint('routes', __name__)


@routes.route("/", methods=["GET", "POST"]) # Home page
def index():
    return render_template("index.html")
