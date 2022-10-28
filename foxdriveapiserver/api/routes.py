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
from utils import Consts, logger
import apps as app
# swagger
swaggeryamls = str(pathlib.Path().absolute()) + "/documents/swagger/"


# sets up base for routs
apibp = Blueprint("apibp", __name__)


# base url
@apibp.route(Consts.base)
def index():

    return "hewwo"

"""
user endpoints 

creates and manages users in the db
"""

# creates users
@apibp.route(Consts.users+"create", methods=["POST"])

def createuser():

    logger.warning(" got request to make new user.....")
    logger.info(" got new user info...")

    user = app.users(**request.json)

    # users db
    user.name = request.json["name"]
    user.userid = request.json["userid"]
    user.create_date = request.json["create_date"]


    if (
        app.db.session.query(app.users).filter_by(name=user.name).scalar()
        is not None
    ):
       
        logger.Error("Entry exsits wont create a new one!")
        return jsonify({"status": "usr in db already", "user": str(user.name)})
       


