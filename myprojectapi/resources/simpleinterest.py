from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse, fields, marshal_with
from datetime import datetime

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('principle_amount', type=float, help='Principal amount must be a number')
parser.add_argument('period', type=float, help='No. of Years must be an integer')
parser.add_argument('rate',choices=(2, 4, 6, 8),type=float,help='Rate must be from given choices: 2,4,6,8')

resource_fields = {
    'simple_interest': fields.Raw,
    'computed_on': fields.DateTime(dt_format='rfc822')
}

class SimpleInterest(Resource):
	
	@marshal_with(resource_fields)
	def post(self):
		args = parser.parse_args()
		p = args['principle_amount']
		n = args['period']
		r = args['rate']
		
		si = (p*n*r)/100.0
		
		return {'simple interest':si, 'computed_on':datetime.now()}