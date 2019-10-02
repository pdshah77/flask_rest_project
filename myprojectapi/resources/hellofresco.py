from flask_restful import Resource

class HelloFresco(Resource):
	def get(self):
		return {'message':'Welcome to Fresco Play!!'},200,{'response_header':'accept/json;v=2'}