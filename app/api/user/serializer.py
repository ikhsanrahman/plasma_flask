import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
    if not string:
        raise ValidationError(" Data cannot be blank")
#end def

class UserSchema(Schema):
    full_name        = fields.String(required=True, validate=cannot_be_blank)
    email            = fields.Email(required=True, validate=cannot_be_blank)
    password         = fields.String(required=True, validate=cannot_be_blank)
    phone_number     = fields.String(required=True, validate=cannot_be_blank)
    gender           = fields.String(required=True, validate=cannot_be_blank)
    alamat           = fields.String(required=True, validate=cannot_be_blank)
    category         = fields.String(required=True, validate=cannot_be_blank)
    jurusan          = fields.String(required=True, validate=cannot_be_blank)
    universitas      = fields.String(required=True, validate=cannot_be_blank)
    # created_at       = fields.Datetime(format=iso)
    # updated_at       = fields.Datetime(format=iso)
    # deleted_at       = fields.Datetime(format=iso)
    # video            = fields.String(load_only)
    # paper            = fields
        
    
    def bool_to_status(self, obj):
        status = "ACTIVE"
        if obj.status != True:
            status = "INACTIVE"
        return status
    #end def

    @validates('full_name')
    def validate_name(self, full_name):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(full_name) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.full_name))
        if len(full_name) > 40:
            raise ValidationError('Invalid {}, max is 40 character'.format(self.full_name))
        if  re.match(pattern, full_name) is None:
            raise ValidationError('Invalid {}. only alphabet is allowed'.format(self.full_name))
    #end def

    @validates('email')
    def validate_created_by(self, email):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(email) < 2:
            raise ValidationError('Invalid email, min is 2 character')
        if len(email) > 40:
            raise ValidationError('Invalid email, max is 40 character')
        if  re.match(pattern, email) is None:
            raise ValidationError('Invalid creator, only Human allowed to create the field, not you')
    #end def

    @validates('password')
    def validate_options(self, password):
        # allow all characters except number
    
        if len(password) < 2:
            raise ValidationError('Invalid password, min is 2 characters')
        if len(password) > 40:
            raise ValidationError('Invalid password, min is 40 character')
        if re.match(pattern, password):
            raise ValidationError('options can not be number at all. see the rule of options')

    @validates('phone_number')
    def validate_name(self, phone_number):
        # allow all character
        pattern = r"^[0-9]+$"
        if len(phone_number) < 2:
            raise ValidationError('Invalid {}. min is 2 character'.format(self.phone_number))
        if len(phone_number) > 40:
            raise ValidationError('Invalid {}}, max is 40 character'.format(self.phone_number))
        if  re.match(pattern, name) is None:
            raise ValidationError('Invalid {}}. only alphabet is allowed'.format(self.phone_number))
    #end def

    @validates('gender')
    def validate_created_by(self, gender):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(gender) < 2:
            raise ValidationError('Invalid gender')
        if len(gender) > 20:
            raise ValidationError('Invalid gender, max is 20 character')
        if  re.match(pattern, gender) is None:
            raise ValidationError('Invalid gender, only Human allowed to create the field, not you')
    #end def

    @validates('alamat')
    def validate_options(self, alamat):
        # allow all characters except number

        pattern = r"^[a-z-A-Z_ ]+$"
        if len(alamat) < 2:
            raise ValidationError('Invalid alamat')
        if len(alamat) > 20:
            raise ValidationError('Invalid alamat, max is 20 character')
        if  re.match(pattern, alamat) is None:
            raise ValidationError('Invalid alamat, only Human allowed to create the field, not you')

    @validates('category')
    def validate_name(self, category):
        # allow all character
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(category) < 2:
            raise ValidationError('Invalid category. min is 2 character')
        if len(category) > 40:
            raise ValidationError('Invalid category, max is 40 character')
        if  re.match(pattern, category) is None:
            raise ValidationError('Invalid category. only alphabet is allowed')
    #end def

    @validates('jurusan')
    def validate_created_by(self, jurusan):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(jurusan) < 2:
            raise ValidationError('Invalid jurusan')
        if len(jurusan) > 20:
            raise ValidationError('Invalid jurusan, max is 20 character')
        if  re.match(pattern, jurusan) is None:
            raise ValidationError('Invalid jurusan, only Human allowed to create the field, not you')
    #end def

    @validates('universitas')
    def validate_options(self, universitas):
        # allow all characters except number

        pattern = r"^[a-z-A-Z_ ]+$"
        if len(universitas) < 2:
            raise ValidationError('Invalid universitas')
        if len(universitas) > 20:
            raise ValidationError('Invalid universitas, max is 20 character')
        if  re.match(pattern, universitas) is None:
            raise ValidationError('Invalid universitas, only Human allowed to create the field, not you')
    #end def

class LoginUserSchema(Schema):
    email               = fields.Email(required=True, validate=cannot_be_blank)
    password            = fields.String(required=True, validate=cannot_be_blank)


class UpdateUserSchema(Schema):
    full_name        = fields.Str(required=True, validate=cannot_be_blank)
    # email 
    # phone_number
    # alamat
    # category
    # jurusan
    # universitas
    # confirm_user
    # status_user
    
    updated_at  = fields.DateTime('%Y-%m-%d %H:%M:%S', load_only=True)

    

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
        # allow all character
        pattern = r"."
        if len(name) < 2:
            raise ValidationError('Invalid name field')
        if len(name) > 40:
            raise ValidationError('Invalid name field, max is 40 character')
        if  re.match(pattern, name) is None:
            raise ValidationError('Invalid name field. Follow the rules')
    #end def

    @validates('created_by')
    def validate_created_by(self, created_by):
        # only allow alphabet character and space
        pattern = r"^[a-z-A-Z_ ]+$"
        if len(created_by) < 2:
            raise ValidationError('Invalid creator')
        if len(created_by) > 20:
            raise ValidationError('Invalid creator, max is 20 character')
        if  re.match(pattern, created_by) is None:
            raise ValidationError('Invalid creator, only Human allowed to create the field, not you')
    #end def

    @validates('options')
    def validate_options(self, options):
        # allow all characters except number

        pattern = r"^[^0-9]+$"
        #put in order
        try :
            list_option = eval(options)
            print(list_option)   
        except:
            raise ValidationError("Options Field is incorrect")

        if not isinstance(list_option, list):
                raise ValidationError("Options must in array")

        for number in list_option :
            if isinstance(number, int):
                raise ValidationError("option is incorrect. number inside not allowed")

        if not list_option :
            raise ValidationError("Options Field is empty")

        if len(options) < 2:
            raise ValidationError('Invalid options')
        if re.match(pattern, options):
            raise ValidationError('options can not be number at all. see the rule of options')

class UpdatePasswordSchema(Schema):
    new_password            = fields.Str(required=True, validate=cannot_be_blank)
    confirm_new_password    = fields.Str(required=True, validate=cannot_be_blank)
