"""
OwO main 
"""
import pathlib
from apps import create_app
from utils import logger, Consts

# this is for running the api
def main():

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + str(pathlib.Path().absolute()) + "/FoxDrive-Data/" + "Data.db"
    )

    app.run(threaded=True, debug=True, host=Consts.url, port=2000)


# this sarts the file
if __name__ == "__main__":
    main()
