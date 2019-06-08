from flask import Blueprint
from flask_restful import Api, Resource

blueprint2 = Blueprint('demo2', __name__)
api = Api(blueprint2)


class Demo2(Resource):

    def get(self):
        return {'Demo': 'Demo2'}


api.add_resource(Demo2, '/demo2')
