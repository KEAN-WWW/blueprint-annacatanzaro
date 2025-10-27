from flask import Flask
from application.bp.homepage import homepage  # Import the Blueprint

def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)  # register blueprint
    return app

if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)

    # Register the Blueprint
    app.register_blueprint(homepage)