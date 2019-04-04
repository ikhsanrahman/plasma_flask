
import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.admin.serializer import *
from app.api.admin.model import AdminProcess
from app.api.request_schema import *

from app.api.config import config

from app.api.namespace import Admin

api = Admin.api


@api.route('/<string:admin_key>/terces/login')
class AdminLogin(Resource):

    @api.doc("admin is monitoring")
    def get(self, admin_key):

        payload = AdminRequestSchema().parser.parse_args(strict=True)

        errors = AdminSchema().load(payload).errors
        if errors:
            return errors
            
        result = AdminProcess().login(payload, admin_key)
        return result
    #end def


# #-------------------------------FILE --------------------------------------------------------#


# @api.route('/<int:admin_key>/terces/list')
# class AdminFile(Resource, admin_key):
    
#     @api.doc('get all list file')
#     def get(self, admin_key):
              
#         list_user = FileProcess().get_files(admin_key)
#         return list_user
#     #end def
 
#     @api.doc('Upload file')
#     def post(self, admin_key):
              
#         upload_file = FileProcess().upload_file(admin_key)
#         return upload_file
#     #end def

#     @api.doc('unactivate file')
#     def delete(self, admin_key):
       
#         unactivate_user = AdminProcess().unactivate_user(admin_key)
#         return unactivate_user
#     #end def

# @api.route('/<str:admin_key>/terces/searchName')
# class Admin(Resource, admin_key):
    
#     @api.doc('search file by title')
#     def get(self, admin_key):
              
#         list_user = AdminProcess().search_user_by_name(admin_key)
#         return list_user
#     #end def

# @api.route('/<str:admin_key>/terces/searchName')
# class Admin(Resource, admin_key):
    
#     @api.doc('search file by title')
#     def get(self, admin_key):
              
#         list_user = AdminProcess().search_user_by_name(admin_key)
#         return list_user
#     #end def

   


# @api.route('/<int:admin_key>/terces/user/unactivateUser')
# class UnactivateUser(Resource):
    
#     @api.doc('unactivate user')
#     def delete(self, admin_key):
       
#         unactivate_user = AdminProcess().unactivate_user(admin_key)
#         return unactivate_user
#     #end def

# @api.route('/<int:admin_key>/terces/user/reactivateUser')
# class ReactivateUser(Resource) :
      
#     def get(self, admin_key) :
#         reactivate_user = AdminProcess().reactivate_user(admin_key)
#         return reactivate_user
#     #end def
# #end class

# @api.route('/<int:admin_key>/terces/file/unactivateFile')
# class UnactivateFile(Resource):
#     #@auth.login_required
#     @api.doc('delete a user')
#     def delete(self, admin_key) :

#         unactivate_file = AdminProcess().unactivate_file(admin_key)
#         return unactivate_file
#     #end def
# #end class

# @api.route('/<int:admin_key>/terces/file/reactivateFile')
# class ReactivateFile(Resource) :
      
#     def get(self, admin_key) :
#         reactivate_file = AdminProcess().reactivate_file(admin_key)
#         return reactivate_file
#     #end def
# #end class


# @api.route('/<int:admin_key>/terces/user/remove')
# class RemoveUser(Resource):

#     def delete(self):
       
#         remove_user = AdminProcess().remove_user(admin_key)
#         return remove_user
#     #end def
# #end class


# @api.route('/<int:admin_key>/terces/file/remove')
# class RemoveFile(Resource):

#     def delete(self):

#         remove_file = AdminProcess().remove_file(admin_key)
#         return remove_file
#     #end def
# #end class

