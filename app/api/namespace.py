from flask_restplus import Namespace, fields

class Home:
	api = Namespace('Home', description='api related to first access')

class User :
	''' class for Data Transfer Operation '''
	api = Namespace('User', description='api related to User')

class Video :
	api = Namespace('score', description='api related to Video ')

class Paper:
	api = Namespace('home', description='api related to Paper')

class Admin:
	api = Namespace('admin', description="api for monitoring apps")

class Info:
	api = Namespace('Info', description="api for info")
