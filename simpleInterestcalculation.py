from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('principle_amount', type=float, help='Principal amount must be a number')
parser.add_argument('period', type=float, help='No. of Years must be an integer')
parser.add_argument('rate',choices=(2, 4, 6, 8),type=float,help='Rate must be from given choices: 2,4,6,8')

class SimpleInterest(Resource):
	
	def post(self):
		args = parser.parse_args()
		p = args['principle_amount']
		n = args['period']
		r = args['rate']
		
		si = (p*n*r)/100.0
		
		return {'simple interest':si}

api.add_resource(SimpleInterest,'/simpleinterest/')

if __name__ == '__main__':
	app.run()