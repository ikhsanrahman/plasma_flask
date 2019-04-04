

from flask_restplus import Api
from flask import Blueprint

from app.api.user.controller import api as user
from app.api.user.controller import home as home
from app.api.file.controller import api as file
from app.api.admin.controller import api as admin
from app.api.info.controller import api as info
# from app.api.score.controller import api as score

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='KRISFI API ',
          version='1.0',
          # description='a engine to score object'
          )


# api.add_namespace(home, path='/')
# api.add_namespace(user, path='/users')
api.add_namespace(file, path='/files')
api.add_namespace(info, path='/info')
api.add_namespace(admin, path='/admin')