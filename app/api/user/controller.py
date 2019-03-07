"""
    Modul of Url field controller that controls all endpoint before come into processing
    _____________________________________________________________________________________

"""

import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.serializers.serializers import( 
                        UserSchema,
                        VideoUserSchema,
                        PaperUserSchema,
                        StoryUserSchema) 
from app.api.errors.errors import bad_request
from app.api.config import config

from app.api.serializers.serializers import UserSchema
from app.api.request_schema import *
from app.api.utilization.dto import User, Home
from app.api.user.views import listUser, registerUser


REQUEST_USER = RegisterUserRequestSchema().parser


api = User.api
home = Home.api

@home.route('')
class Home(Resource):
    """ first index slash (/) """
    def get(self) :
        return jsonify(message="Welcome to Plasma Lab Platform")
    #end def
#end class
    
@api.route('')
class User(Resource):
   
    @api.doc('list of user')
    def get(self):
        """List all fields"""
        return listUser()
    #end def

    @api.doc('register a new user')
    def post(self):
        """Creates a new field """
        #request data in form-data not json form
        data = REQUEST_USER.parse_args()
        errors = UserSchema().validate(data)
        if errors :
            return bad_request(errors)
        #end if

        responses = registerUser(data=data)
        return responses
    #end def
  
    @api.doc('update the user')
    def put(self):
        """ Updates a Field """
        #request data in form-data not json form
        data = request.form

        errors = EditFieldSchema().validate(data)
        if errors :
            return bad_request(errors)
        #end if

        updated_field = updateField(data=data)
        return updated_field
    #end def


    @api.doc('delete a field')
    def delete(self) :
        """ Delete a Field """
        data = request.form
        #request data in form-data not json form
        errors = DeleteFieldSchema().validate(data)
        if errors :
            return bad_request(errors)
        #end if

        deletefield = deleteField(data=data)
        return deletefield
    #end def
#end class

@api.route('/login')
class LoginUser(Resource):
    def get(self):
        data = LoginUserRequestSchema().parser_args(strict=True)
        errors = UserSchema.validate(data)
        if errors :
            return "login error"

        result = loginUser(data)
        return result

