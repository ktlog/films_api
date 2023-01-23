from flask_restful import Resource
from flask import request
from marshmallow.exceptions import ValidationError

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema
from src.services.actor_service import ActorService


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actors = ActorService.fetch_all_actors(session=db.session)
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return '', 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 404
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def delete(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return {'message': 'wrong data'}, 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
