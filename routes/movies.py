from flask import jsonify, Blueprint
from auth import requires_auth
from models.movie import Movie
bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('/', methods=['GET'])
@requires_auth('get:movies')
def get_movies():
    page = request.args.get('page', default='1', type=int)
    per_page = request.args.get('per_page', default='10', type=int)
    movies = movies.query.paginate(
        page=page, per_page=per_page)
    return jsonify({
        "success": True,
        "movies": [
            movie.toDict() for movie in movies
        ],
        'code': 200
    }), 200


@bp.route('/<id:int>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({
        "success": True,
        "actors": [movie.toDict()]
        'code': 200,
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:movies')
def post_movies():
    json_data = request.json
    title = json_data['title']
    release_date = json_data['release_date']
    new_movie = Movie(title=title, release_date=release_date)
    session = db.session
    try:
        db.session.add(new_actor)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": Exception.__repr__(),
            'code': 500,
        }), 500
    finally:
        db.session.close()

    return jsonify({
        "success": True,
        "movies": [new_actor.toDict()]
    }), 201


@bp.route('/', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movies():
    json_data = request.json
    movie = Movie.query.get(id)
    Movie.update(json_data)
    return jsonify({
        "success": True,
        "movies": [actor.toDict()]
    }), 200
