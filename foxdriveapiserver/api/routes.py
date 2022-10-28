"""
routs for the server
"""

from functools import wraps
from importlib.resources import path
import os
from flasgger import swag_from
from crypt import methods
from datetime import datetime
import json

from pyexpat import model
from urllib import response
from xmlrpc.client import DateTime
from flask import Blueprint, abort
from flask import (
    jsonify,
    render_template,
    redirect,
    request,
    url_for,
    send_from_directory,
    send_file,
)

from datetime import datetime
import pathlib


# swagger
swaggeryamls = str(pathlib.Path().absolute()) + "/documents/swagger/"


# sets up base for routs
apibp = Blueprint("apibp", __name__)


# base url
@apibp.route("/")
def index():

    return "hewwo"
