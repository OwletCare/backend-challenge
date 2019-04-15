from flask import Flask
from flask_restplus import Api, Resource

service_name = 'coding-test'
service_description = 'Test to eval candidates'

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title=service_name,
    description=service_description,
)
ns = api.namespace('/', description='default operations')


@ns.route('/hello/')
class GenericService(Resource):
    def get(self):
        return "Mike"

    def post(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
