"""
    Modul of Url field controller that controls all endpoint before come into processing
    _____________________________________________________________________________________

"""

import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.serializer import CreateFieldSchema, EditFieldSchema, DeleteFieldSchema, ReactivateFieldSchema, RemoveFieldSchema, SearchFieldSchema
from app.api.errors import bad_request
from app.api.config import config

from app.api.utilization.dto import FieldsDto, Home
from app.api.field.model import addFields, getFields, searchField, updateField, deleteField, activateField, removeField
from app.api.validation.validation import ValidField
from app.api.authorization import authorization as auth

RESPONSES_MSG = config.Config.RESPONSES_MSG

api = FieldsDto.api
home = Home.api
validOptions = ValidField()

@home.route('')
class Home(Resource):
    """ first index slash (/) """
    def get(self) :
        return jsonify(message="Welcome to Credit Score Engine, let's explore deeper")
    #end def
#end class
    
@api.route('')
class Fields(Resource):
    ''' 
        This class only for CRUD of fields
        __________________________________ 
    '''
    @auth.token_required
    @api.doc('list_of_fields')
    def get(self):
        """List all fields"""
        return getFields()
    #end def

    @auth.token_required
    @api.doc('create a new field')
    def post(self):
        """Creates a new field """
        #request data in form-data not json form
        data = request.form
        errors = CreateFieldSchema().validate(data)
        if errors :
            return bad_request(errors)
        #end if

        responses = addFields(data=data)
        return responses
    #end def

    @auth.token_required   
    @api.doc('update the field')
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


    @auth.token_required
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

@api.route('/searchField')
class Field(Resource) :
    """
        class to handle to get one field
        ________________________________
    """ 
    @auth.token_required
    @api.doc('search field')
    def get(self) :
        ''' Get one Field '''

        data = request.form
        #request data in form-data not json form
        errors = SearchFieldSchema().validate(data)
        if errors :
           return bad_request(errors)
        #end if

        oneField = searchField(data=data)
        return oneField
    #end def
#end class


@api.route('/activate')
class ActivateField(Resource) :
    """
        class to activate any field 
        ___________________________
    """

    @auth.token_required
    def post(self) :
        ''' post to activate the field '''
        data = request.form 
        #request data in form-data not json form
        errors = ReactivateFieldSchema().validate(data)
        if errors :
            return bad_request(errors)
        #end if

        activate_field = activateField(data)
        return activate_field
    #end def
#end class

@api.route('/remove')
class RemoveField(Resource):
    """
        Remove one field that is needed
        _______________________________ 
    """

    @auth.token_required
    def post(self):
        """ post method to post that field need to be removed """
        #request data in form-data not json form
        data = request.form
        
        errors = RemoveFieldSchema().validate(data)
        if errors:
            return bad_request(errors)
        #end if

        remove_field = removeField(data)
        return remove_field
    #end def
#end class

@api.route('/login')
class Login(Resource) :
    ''' class to get dummy token for authentication '''
    def get(self):
        auth = request.authorization

        if not auth or not auth.username  or not auth.password :
            return make_response("could not verify", 401, {'WWW-Authenticate' : 'Basic realm="Login Required!"'})
        #end if

        token =jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90)}, config.Config.SECRET_KEY)

        return jsonify(token=token.decode('UTF-8'))
    #end def
#end class
