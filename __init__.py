from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints or configure app if needed
    # from .api import api_bp
    # app.register_blueprint(api_bp)

    return app