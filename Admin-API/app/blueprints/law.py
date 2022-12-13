from flask import Blueprint, g, jsonify, request
from app.models.law import Law

lawbp = Blueprint('law', __name__)


@lawbp.route('/', methods=['GET'])
def all():
    laws = g.db.query(Law).all()
    return jsonify([law.as_dict() for law in laws])

@lawbp.route('/<id>', methods=['GET'])
def one(id):
    law = g.db.query(Law).filter(Law.id == id).one()
    return jsonify(law.as_dict())

@lawbp.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    law = Law(**data)
    g.db.add(law)
    g.db.commit()
    return "Ok"

@lawbp.route('/<id>', methods=['DELETE'])
def delete(id):
    law = g.db.query(Law).filter(Law.id == id).one()
    g.db.remove(law)
    g.db.commit()
    return "Ok"

@lawbp.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    law = g.db.query(Law).filter(Law.id == data['id']).one()
    for key in data:
        law[key] = data[key]
    g.db.commit()
    return "Ok"
