from flask import request, Blueprint
from flask_restful import Resource, abort, Api

playcourses_bp = Blueprint('PlayCoursesAPI', __name__)
playcourses_api = Api(playcourses_bp)

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
		
playcourses_api.add_resource(PlayCourse, '/Courses/', '/Courses/<int:course_id>')