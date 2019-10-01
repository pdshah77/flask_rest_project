from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)
play_courses = {}

class PlayCourse(Resource):
	
	def post(self,course_id):
		if course_id not in play_courses:
			play_courses[course_id] = request.form['course_name']
			return {course_id:play_courses[course_id]}
		abort(404, message="Course_Id {} already exists.".format(course_id))
		
	def get(self,course_id=None):
		if course_id is None:
			return play_courses
		elif course_id not in play_courses:
			abort(404, message="Course_Id {} doesn't exists.".format(course_id))
		else:
			return {course_id:play_courses[course_id]}
		
	def delete(self,course_id):
		if course_id in play_courses:
			response = '{} is deleted.'.format(play_courses[course_id])
			del play_courses[course_id]
			return response
		abort(404,message="Course_Id {} doesn't exists.".format(course_id))
		
	def put(self,course_id):
		if course_id not in play_courses:
			abort(404, message="Course_Id {} doesn't exist.".format(course_id))
		play_courses[course_id] = request.form['course_name']
		return {course_id: play_courses[course_id]}
	
api.add_resource(PlayCourse,'/Courses/','/Courses/<int:course_id>')

if __name__ == '__main__':
	app.run()