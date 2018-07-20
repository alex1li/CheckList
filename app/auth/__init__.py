# app/admin/__init__.py
# 07/19/18
# https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views