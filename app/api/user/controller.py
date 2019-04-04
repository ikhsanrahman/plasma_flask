
import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.user.serializer import *
from app.api.user.model import UserProcess
from app.api.request_schema import *

from app.api.config import config

from app.api.namespace import User, Home

# RESPONSES_MSG = config.Config.RESPONSES_MSG
api = User.api
home = Home.api

 

@home.route('')
class Home(Resource):
   
    def get(self) :
        responses = {}
        responses['Entry Gate'] = "Welcome to Krisfi (Kelompok Riset Fisika)" 
        return jsonify(Opening=responses)
    
@api.route('/login')
class Login(Resource) :
    def get(self):
        payload = LoginUserRequestSchema().parser.parse_args(strict=True)
        if payload['password'] != payload['confirm_password']:
            return "password doesnt not match"
            
        errors = LoginUserSchema().load(payload).errors
        if errors:
            return errors

        result = UserProcess().login(payload)

        return result

# @api.route('/<int:user_id>/search')
# class SearchIdUser(Resource) :

#     @api.doc('search user by id')
#     def get(self, user_id) :

#         user = UserProcess().search_user_by_id(user_id)
#         return user
#     #end def
# #end class

# @api.route('/search')
# class SearchNameUser(Resource) :

#     @api.doc('search user by name')
#     def get(self) :
#         payload = SearchUserRequestSchema().parser.parse_args(strict=True)

#         user = UserProcess().search_user_by_name(payload)
#         return user
#     #end def
# #end class

@api.route('')
class Users(Resource):
   
    # @api.doc('get all user')
    # def get(self):

    #     result = UserProcess().get_users() 
    #     return result
    # #end def

    @api.doc('registering new user')
    def post(self):
        
        payload = UserRequestSchema().parser.parse_args(strict=True)

        if payload['password'] != payload['confirm_password']:
            return "the password not match"

        errors = UserSchema().load(payload).errors
        if errors :
            return errors


        result = UserProcess().create_user(payload)
        return result
    #end def

@api.route('/<int:user_id>/updateUser')
class EditUser(Resource):
    
    @api.doc('update a user')
    def put(self, user_id):
       
        payload = UpdateUserRequestSchema().parser.parse_args(strict=True)

        errors = EditUserSchema().load(payload).errors
    
        if errors :
            return errors
        

        edit_user = UserProcess().update_user(payload, user_id)
        return edit_user
    #end def

@api.route('/<int:user_id>/editPassword')
class EditPasswordUser(Resource):
    
    @api.doc('edit password user')
    def put(self, user_id):
       
        payload = UpdatePasswordRequestSchema().parser.parse_args(strict=True)

        if payload['new_password'] != payload['confirm_new_password'] :
            return "not match"

        errors = UpdatePasswordSchema().load(payload).errors
    
        if errors :
            return errors
        

        edit_user = UserProcess().update_password_user(payload, user_id)
        return edit_user
    #end def

# @api.route('/<int:user_id>/unactivate')
# class UnactivateUser(Resource):
#     #@auth.login_required
#     @api.doc('delete a user')
#     def delete(self, user_id) :

#         delete = UserProcess().unactivate_user(user_id)
#         return delete
#     #end def
# #end class



# @api.route('/<int:user_id>/reactivate')
# class ReactivateUser(Resource) :
      
#     def get(self, user_id) :
#         result = UserProcess().reactivate_user(user_id)
#         return result
#     #end def
# #end class

# @api.route('/remove')
# class RemoveUser(Resource):

#     def get(self):
#         """ post method to post that field need to be removed """
#         #request data in form-data not json form


#         remove_field = removeField(data)
#         return remove_field
#     #end def
# #end class

# @api.route('/destroyDatabase')
# class destroyDatabase(Resource):
   

#     # @auth.login_required
#     def post(self):
#         return destroyDatabase()

#     #end def
# #end class




