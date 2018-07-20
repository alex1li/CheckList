# app/home/__init__.py
# 07/18/18
# https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views