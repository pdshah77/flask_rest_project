from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class HelloFresco(Resource):
	def get(self):
		return {'message':'Welcome to Fresco Play!!'},200,{'response_header':'accept/json;v=2'}
	
api.add_resource(HelloFresco,'/','/home/','/index/')

if __name__ == '__main__':
	app.run()