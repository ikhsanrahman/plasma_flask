'''
	A module for define api for fields, score and home
	__________________________________________________
'''


from flask_restplus import Namespace, fields

class User :
	''' class for Data Transfer Operation '''
	api = Namespace('user', description='fields related to operations')

class ScoreDto :
	api = Namespace('score', description='fields are used to score ')

class Home:
	api = Namespace('home', description='index slash to welcome')

