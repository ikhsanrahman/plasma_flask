""" 
    This is module to model every part related to field process
    ______________________________________________________________
"""
#import dependencies
import os
import datetime
 
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
                LoginManager, 
                UserMixin, 
                login_user, 
                login_required, 
                logout_user, 
                current_user)

from app.api.serializers.serializers import UserSchema
from app.api.errors.errors import bad_request, method_not_allowed, request_not_found, internal_error

from app.api.config import config
from app.api.create_app import db
from app.api.db_model import *


def registerUser(data) :
    ''' 
        function to create new fields 
        _____________________________
    '''

    field = {}
    options = {}
    responses = {}

    field['name'] = data['name']
    field['email'] = data['email']
    field['password'] = data['password']

    #check whether field exists or not
    user = User.query.filter_by(name=field['name']).first()

    

    new_user = User(name=field['name'], email=field['email'], password=[field['password']])
    new_user.set_status_user(True)
    db.session.add(new_user)
    db.session.commit()
    return "register success"
    #end if
#end def

def login(data) :
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if user and user.check_password_hash(password) :
        user.set_status_user(True)
        return "login has succeed. this is your id user {}".format(user.id)



def listUser():
    users = User.query.all()
    output = []
    responses = {}
    
    
        #if user.status_user == True :
    result = UserSchema(many=True).dump(users).data
    return jsonify(output=result)
#end def

def searchField(data):
    ''' 
        function for get one field 
        __________________________
    '''
    responses = {}
    output_ = []
    name = data['name'].lower()
    #if name existed
    fields = db.find()
    for field in fields :
        if name in field['name'].split():
            output = {'name' : field['name'], 'options' : field['options']}
            output_.append(output)
        #end if
    #end for
        
    if output_:
        return jsonify(output=output_)
    #end if

    if not output_:
        responses['messages'] = RESPONSES_MSG['FAILED']['NO_FIELD']
        return bad_request(responses)
    #end if
#end def

def updateField (data) :
    ''' 
        function to update field that has a miss
        _________________________________________ 
    '''
    field = {}
    responses = {}

    field['name'] = data['name']
    field['new_name'] = data['new_name']
    field['updated_by'] = data['updated_by']
    field['new_options'] = eval(data['new_options'])

    field_ = db.find_one({"name": field['name'].lower()})
    #if field existed
    if field_ :
        for option in field['new_options'] :
            #if 'type' and 'select' doesn't exist in option
            if 'type' not in option.keys() or 'select' not in option.keys() :
                responses['messages'] = RESPONSES_MSG['FAILED']['INVALID_OPTIONS_PATTERN'] 
                return bad_request(responses)
            option['type'] = option['type'].lower()
            if valid.validateFieldType(option) == True :
                update_field = helper.update_field(field)
                return update_field 
            else :
                responses['messages'] = RESPONSES_MSG['FAILED']['UPDATED_INVALID']
                return method_not_allowed(responses)
            #end if
        #end for
    #end if
    #if field doesn't exist
    if not field_ :
        responses['messages'] = RESPONSES_MSG['FAILED']['NO_FIELD']
        return responses
    #end if
#end def

def activateField(data) :
    ''' 
        function to activate a field that will be used
        ______________________________________________ 
    '''
    field = {}
    responses = {}

    field['name'] = data['name']
    field['activated_by'] = data['activated_by']

    field_ = db.find_one({"name": field['name'].lower()})
    #if field existed and status not active (false = not active)
    if field_ and field_['status'] == False :
        activate_field = helper.activate_field(field)
        return activate_field
    else :
        responses['messages'] = RESPONSES_MSG['FAILED']['ACTIVATION_FIELD']
        return request_not_found(responses)
    #end if
#end def

def deleteField(data) :
    ''' 
        function to hide/edit a field 
        ______________________________
    '''
    field = {}
    responses = {}
    field['name'] = data['name']
    field['deleted_by'] = data['deleted_by']

    field_ = db.find_one({"name": field['name'].lower()})
    #if field existed
    if field_ and field_['status'] == True :
        delete_field = helper.delete_field(field)
        return delete_field
    else :
        responses['messages'] = RESPONSES_MSG['FAILED']['DELETION_FIELD']
        return request_not_found(responses)
    #end if
#end def

def removeField(data) :
    ''' 
        function to remove field from database 
        _______________________________________
    '''
    field = {}
    responses = {}
    field['name'] = data['name']
    field['removed_by'] = data['removed_by']

    field_ = db.find_one({"name": field['name'].lower()})
    #if field existed
    if field_ :
        remove_field = helper.remove_field(field)
        return remove_field
    else :
        responses['messages'] = RESPONSES_MSG['FAILED']['REMOVE_FIELD']
        return request_not_found(responses)
    #end if
#end def