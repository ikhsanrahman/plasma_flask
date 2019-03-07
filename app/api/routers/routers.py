''' 
	module of collection of all routes
	__________________________________ 
'''


from flask_restplus import Api
from flask import Blueprint

from app.api.user.controller import api as user
from app.api.user.controller import home as home

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CREDIT SCORE API ',
          version='1.0',
          description='a engine to score object'
          )

#set endpoints to be added to url
#before add this, add url_prefix http:localhost:5555/api/v1/{{choose one of below}}
api.add_namespace(home, path='/')
api.add_namespace(user, path='/user')