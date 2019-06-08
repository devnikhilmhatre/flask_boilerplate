from flask import Blueprint
from flask_restful import Api, Resource

blueprint1 = Blueprint('demo1', __name__)
api = Api(blueprint1)


class Demo1(Resource):

    def get(self):
        return {'Demo': 'Demo1'}


api.add_resource(Demo1, '/demo1')
