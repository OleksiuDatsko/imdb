import logging
import dotenv
import os

from imdb import create_app

dotenv.load_dotenv()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    config_data = {
        "DEBUG": os.getenv("DEBUG"),
        "SQLALCHEMY_TRACK_MODIFICATIONS": os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS"),
        "SQLALCHEMY_DATABASE_URI": os.getenv("SQLALCHEMY_DATABASE_URI"),
    }

    create_app(config_data).run(
        port=int(os.getenv("APP_PORT", "8000")),
        debug=True,
        host="0.0.0.0",
    )
