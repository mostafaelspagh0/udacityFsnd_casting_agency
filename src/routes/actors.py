from flask import jsonify, Blueprint, request, abort
from flask_sqlalchemy import BaseQuery
from auth.enums import Permissions
from src.auth import requires_auth
from src.database import Actor, db


bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('/', methods=['GET'])
@requires_auth(Permissions.get_actors)
def get_actors(payload):
    page = int(request.args.get('page', default='1', type=int))
    per_page = int(request.args.get('per_page', default='10', type=int))
    actors = db.session.query(Actor).order_by(Actor.id).paginate(
        page=page, per_page=per_page).items
    return jsonify({
        "success": True,
        "actors": [
            actor.toDict() for actor in actors
        ],
        'code': 200
    }), 200


@bp.route('/<int:id>', methods=['GET'])
@requires_auth(Permissions.get_actors)
def get_actors_by_id(payload, id):
    actor: Actor = Actor.query.get(int(id))
    if actor is None:
        abort(404)
    else:
        return jsonify({
            "success": True,
            "actors": [actor.toDict()],
            'code': "SUCCESS",
        }), 200


@bp.route('/<int:id>', methods=['DELETE'])
@requires_auth(Permissions.delete_actors)
def delete_actors(payload, id):
    actor: Actor = Actor.query.get(int(id))
    if actor is None:
        abort(404)

    error = None

    try:
        actordict = actor.toDict()
        db.session.delete(actor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        error = e
    finally:
        db.session.close()

    if error is None:
        return jsonify({
            "success": True,
            "actors": [actordict],
            'code': "DELETED",
        }), 202
    else:
        abort(500)


@bp.route('/', methods=['POST'])
@requires_auth(Permissions.add_actors)
def post_actors(payload):
    json_data = request.json
    name = json_data['name']
    age = json_data['age']
    gender = json_data['gender']
    new_actor = Actor(name=name, age=age, gender=gender)
    error = False
    try:
        db.session.add(new_actor)
        db.session.commit()
        actor_dict = new_actor.toDict()
    except Exception as k:
        e = k
        db.session.rollback()
        error = True
    finally:
        db.session.close()

    if not error:
        return jsonify({
            "success": True,
            'code': 'created',
            "actors": [actor_dict]
        }), 201
    else:
        abort(500)


@bp.route('/<int:id>', methods=['PATCH'])
@requires_auth(Permissions.patch_actors)
def patch_actors(payload, id):
    json_data = request.json
    actorQuery: BaseQuery = db.session.query(Actor).filter_by(id=id)
    actor: Actor = actorQuery.one_or_none()
    if actor is None:
        abort(404)
    actorQuery.update(json_data)
    db.session.commit()
    return jsonify({
        "success": True,
        "actors": [actor.toDict()],
        "code": "UPDATED"
    }), 202
