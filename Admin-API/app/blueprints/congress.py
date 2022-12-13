from flask import Blueprint, g, jsonify, request
from app.models.congress import Congress

congressbp = Blueprint('congress', __name__)


@congressbp.route('/', methods=['GET'])
def all():
    congresss = g.db.query(Congress).all()
    return jsonify([congress.as_dict() for congress in congresss])

@congressbp.route('/<id>', methods=['GET'])
def one(id):
    congress = g.db.query(Congress).filter(Congress.id == id).one()
    return jsonify(congress.as_dict())

@congressbp.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    congress = Congress(**data)
    g.db.add(congress)
    g.db.commit()
    return "Ok"

@congressbp.route('/<id>', methods=['DELETE'])
def delete(id):
    congress = g.db.query(Congress).filter(Congress.id == id).one()
    g.db.remove(congress)
    g.db.commit()
    return "Ok"

@congressbp.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    congress = g.db.query(Congress).filter(Congress.id == data['id']).one()
    for key in data:
        congress[key] = data[key]
    g.db.commit()
    return "Ok"
