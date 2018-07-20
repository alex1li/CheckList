# app/admin/__init__.py
# 07/18/18
# https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views