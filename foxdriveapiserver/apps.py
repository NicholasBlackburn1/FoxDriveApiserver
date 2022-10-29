"""
routs for the api server
"""


import pathlib
from flasgger import Swagger
from pathlib import Path
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from utils import logger, Consts
from api import routes



db = SQLAlchemy()

# the user db
class users(db.Model):
    __tablename__ = "Users"
    __table_args__ = {"sqlite_autoincrement": True}

    userid = db.Column(db.String(255),primary_key=True)
    name =  db.Column(db.String(255))
    create_date =  db.Column(db.String(255))


# event db
class events(db.Model):
    __tablename__ = "capturedevents"
    __table_args__ = {"sqlite_autoincrement": True}

    # colomes 
    userid = db.Column(db.String(255),primary_key=True)
    eventid = db.Column(db.String(255))
    fired_time = db.Column(db.String(255))


class userspoints(db.Model):

    __tablename__ = "userspoints"
    __table_args__ = {"sqlite_autoincrement": True}

    # colomes 
    userid = db.Column(db.String(255),primary_key=True)
    Last_eventid = db.Column(db.String(255))
    current_points = db.Column(db.String(255))





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




# this makes the local file paths for storing the data
def makePaths():


    if Path(str(Path().absolute()) + Consts.basepath).exists:
        # base bath
        logger.info("creating file structure for prgram...")

        Path(str(Path().absolute()) + Consts.basepath).mkdir(
            parents=True, exist_ok=True
        )

        # avi paths
        Path(str(Path().absolute()) + Consts.collectedimages).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.collectedvideos).mkdir(
            parents=True, exist_ok=True
        )

        logger.PipeLine_Ok("created paths successfully")

    else:
        logger.warning("the paths exist cannot create them uwu~")


#! creates the tweb app 
def create_app():

    #! created paths
    logger.info("creating the folder patjhs...")
    makePaths()
    

    example_blueprint = Blueprint("example_blueprint", __name__)

    # creates the flask app
    logger.Warning("Creating flask app...")
    app = Flask(
        __name__, static_url_path="/files", static_folder="FoxDrive-Data/static"
    )

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
