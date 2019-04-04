import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class UserSchema(Schema):
    name                        = fields.Str(required=True, validate=cannot_be_blank)
    email                       = fields.Str(required=True, validate=cannot_be_blank)
    password                    = fields.Str(required=True, validate=cannot_be_blank)
    occupation                  = fields.Str()
    phone_number                = fields.Str()
    alamat                      = fields.Str()
    interesting_field           = fields.Str()
    status_user                 = fields.Method("bool_to_status")
    created_at                  = fields.DateTime('%Y-%m-%d %H:%M:%S', load_only=True)


    class Meta():
        pass

    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status != True:
            status = "INACTIVE"
        return status
    #end def

    @post_load
    def crated_field(self, data):
        return db(**data)
    #end def

    @validates('name')
    def validate_name(self, name):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(name) < 2:
            raise ValidationError('Invalid username')
        if len(name) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, name) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def

    @validates('email')
    def validate_name(self, email):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(email) < 2:
            raise ValidationError('Invalid username')
        if len(email) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, email) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def

    @validates('password')
    def validate_name(self, password):
        # only allow alphabet character and space
        pattern = r"."
        if len(password) < 2:
            raise ValidationError('Invalid username')
        if len(password) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, password) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def



class VideoUserSchema(Schema):
    judul_video                 = fields.Str(required=True, validate=cannot_be_blank)
    description                 = fields.Str(required=True, validate=cannot_be_blank)
    created_at                  = fields.DateTime('%Y-%m-%d %H:%M:%S', load_only=True)


    class Meta():
        pass

    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status != True:
            status = "INACTIVE"
        return status
    #end def

    @post_load
    def crated_field(self, data):
        return db(**data)
    #end def

    @validates('judul_video')
    def validate_name(self, judul_video):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(judul_video) < 2:
            raise ValidationError('Invalid username')
        if len(judul_video) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, judul_video) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def


    @validates('description')
    def validate_name(self, description):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(description) < 2:
            raise ValidationError('Invalid username')
        if len(description) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, description) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def


class PaperUserSchema(Schema):
    judul_paper                     = fields.Str(required=True, validate=cannot_be_blank)
    description                     = fields.Str(required=True, validate=cannot_be_blank, load_only=True)
    created_at                      = fields.DateTime('%Y-%m-%d %H:%M:%S', load_only=True)


    class Meta():
        pass

    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status != True:
            status = "INACTIVE"
        return status
    #end def

    @post_load
    def crated_field(self, data):
        return db(**data)
    #end def

    @validates('judul_paper')
    def validate_name(self, judul_paper):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(judul_paper) < 2:
            raise ValidationError('Invalid username')
        if len(judul_paper) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, judul_paper) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def

    @validates('description')
    def validate_created_by(self, description):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(description) < 2:
            raise ValidationError('Invalid creator')
        if len(description) > 40:
            raise ValidationError('Invalid creator, max is 40 character')
        if  re.match(pattern, description) is None:
            raise ValidationError('Invalid creator, only alphabet allowed')


class StoryUserSchema(Schema):
    name            = fields.Str(required=True, validate=cannot_be_blank)
    activated_by    = fields.Str(required=True, validate=cannot_be_blank, load_only=True)
    activated_at    = fields.DateTime('%Y-%m-%d %H:%M:%S', load_only=True)
    status          = fields.Method("bool_to_status")

    class Meta():
        pass

    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status != True:
            status = "INACTIVE"
        return status
    #end def

    @post_load
    def crated_field(self, data):
        return db(**data)
    #end def

    @validates('name')
    def validate_name(self, name):
        # only allow alphabet character and space
        pattern = r"^[a-zA-Z ]+$"
        if len(name) < 2:
            raise ValidationError('Invalid username')
        if len(name) > 40:
            raise ValidationError('Invalid username, max is 40 character')
        if  re.match(pattern, name) is None:
            raise ValidationError('Invalid field, only alphabet allowed')
    #end def
