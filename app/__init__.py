from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    load_dotenv()

    from .routes import main
    app.register_blueprint(main)

    return app