from flask import Blueprint, g, jsonify, request
from app.models.topic import Topic

topicbp = Blueprint('topic', __name__)


@topicbp.route('/', methods=['GET'])
def all():
    topics = g.db.query(Topic).all()
    return jsonify([topic.as_dict() for topic in topics])

@topicbp.route('/<id>', methods=['GET'])
def one(id):
    topic = g.db.query(Topic).filter(Topic.id == id).one()
    return jsonify(topic.as_dict())

@topicbp.route('/', methods=['POST'])
def create():
    data = request.get_json(force=True)
    topic = Topic(**data)
    g.db.add(topic)
    g.db.commit()
    return "Ok"

@topicbp.route('/<id>', methods=['DELETE'])
def delete(id):
    topic = g.db.query(Topic).filter(Topic.id == id).one()
    g.db.remove(topic)
    g.db.commit()
    return "Ok"

@topicbp.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    topic = g.db.query(Topic).filter(Topic.id == data['id']).one()
    for key in data:
        topic[key] = data[key]
    g.db.commit()
    return "Ok"
