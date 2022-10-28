"""
routs for the api server
"""


import pathlib
from flasgger import Swagger
from pathlib import Path
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from utils import logger
from api import routes


db = SQLAlchemy()



# this cofigs the db
def configure_database(app, db):
    @app.before_first_request
    def initialize_database():
        logger.warning("Creating db... ")

        db.create_all()
        db.session.commit()

        logger.PipeLine_Ok("created db successfully.")

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app():

    #! created paths
    logger.info("creating the folder patjhs...")
    

    example_blueprint = Blueprint("example_blueprint", __name__)


    # creates the flask app
    logger.Warning("Creating flask app...")
    app = Flask(__name__, static_url_path="/files",
                static_folder="FoxDrive-Data/static")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + str(pathlib.Path().absolute()) + "/FoxDrive-Data/" + "Data.db"
    )

    
    logger.PipeLine_Ok("started flaskapp")

    logger.info("registered blueprints")

    
    app.register_blueprint(example_blueprint)
    app.register_blueprint(routes.apibp)
    logger.PipeLine_Ok("REGISTERED blueprints")

    logger.info("setting foxdrive database..")
    configure_database(app, db)
    db.init_app(app)
    return app
