import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db

def cannot_be_blank(string):
	if not string:
		raise ValidationError(" Data cannot be blank")
#end def

class AdminSchema(Schema):
    name               = fields.String(required=True, validate=cannot_be_blank)
    password            = fields.String(required=True, validate=cannot_be_blank)

    @validates('name')
    def validate_email(self, name):
        # only allow alphabet character and space
        pattern = r"."
        if len(name) < 2:
            raise ValidationError('Invalid name, min is 2 character')
        if len(name) > 40:
            raise ValidationError('Invalid name, max is 40 character')
        if re.match(pattern, name) is None:
            raise ValidationError('Invalid creator, only Human allowed to create the field, not you')
    #end def

    @validates('password')
    def validate_password(self, password):
        # allow all characters except number
        pattern = r"."
        if len(password) < 2:
            raise ValidationError('Invalid password, min is 2 characters')
        if len(password) > 40:
            raise ValidationError('Invalid password, min is 40 character')
        if re.match(pattern, password) is None:
            raise ValidationError('invalid password')
    #end def
#end class