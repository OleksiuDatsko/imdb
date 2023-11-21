import logging
import dotenv
import os

from imdb import create_app

dotenv.load_dotenv()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    config_data = {
        "DEBUG": os.getenv("DEBUG") == "True",
        "SQLALCHEMY_TRACK_MODIFICATIONS": os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
        == "True",
        "SQLALCHEMY_DATABASE_URI": os.getenv("SQLALCHEMY_DATABASE_URI"),
    }
    print(config_data, flush=True)
    create_app(config_data).run(
        port=int(os.getenv("APP_PORT", "8000")),
        debug=True,
        host=os.getenv("APP_HOST", "localhost"),
    )
