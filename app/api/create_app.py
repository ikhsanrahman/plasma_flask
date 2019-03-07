''' 
	this module to create application from create function 
'''

import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


from app.api.config.config import config_by_name
#from app.api.routers.routers import blueprint

def page_not_found(e):
	error = jsonify({
			"error" 		: "Ooooopppp, where are you going ?, You are in wrong page",
			"description"	: "please check in right spelling of URL that you want to dive "
	})
	return error, 404

def create_app(config_name) :
	app = Flask(__name__)
	app.config.from_object(config_by_name[config_name])
	db.init_app(app)
	app.register_error_handler(404, page_not_found)
	return app