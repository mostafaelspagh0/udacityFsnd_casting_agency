from flask import jsonify, Blueprint
from auth import requires_auth
bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('/', methods=['GET'])
@requires_auth('get:actors')
def get_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:actors')
def post_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['PATCH'])
@requires_auth('patch:actors')
def get_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200
