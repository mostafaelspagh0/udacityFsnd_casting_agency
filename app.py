from flask import Flask
from flask.json import jsonify
from db import setup_db, setup_migration
from routes import *
from auth import AuthError


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.url_map.strict_slashes = False
    setup_db(app)

    # register models
    from models import Actor, Movie
    app.register_blueprint(actors_router)
    app.register_blueprint(movies_router)

    @app.route('/', methods=['GET'])
    def healthy():
        return "healthy"

    @app.errorhandler(AuthError)
    def handle_bad_request(e):
        return jsonify({
            "success": False,
            "error" : "UNAUTHORIZED",
            'code': 401,
        }), 401
    return app
