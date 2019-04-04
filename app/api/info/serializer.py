import re

from marshmallow import Schema, fields, ValidationError, post_load, validates
from app.api.create_app import db


def cannot_be_blank(string):
	if not string:
		raise ValidationError(" Data cannot be blank")
#end def

class InfoSchema(Schema):
	id               	  = fields.Integer()
	title	     	 	  = fields.String(required=True, validate=cannot_be_blank)
	name_file_1       = fields.Method("get_video")
	name_file_2       = fields.Method("get_paper")
	description 		  = fields.String(required=True, validate=cannot_be_blank)
	status                = fields.Method("convert_bool_to_str")
	time_created          = fields.DateTime(attribute="time_created")
	time_updated          = fields.DateTime(attribute="time_updated")
	time_deleted          = fields.DateTime(attribute="time_deleted")
	admin_id			      = fields.Integer()
		
	
	def get_paper(self, obj):
		if obj.name_file_paper:
			return obj.name_file_1

	def get_video(self, obj):
		if obj.name_file_video:
			return obj.name_file_2


	def convert_bool_to_str(self, obj):
		status = "ACTIVE"
		if obj.status != True:
			status = "INACTIVE"
		return status
	#end def

	@validates('title')
	def validate_title(self, title):
		
		pattern = r"^[a-z-A-Z0-9_ ]+$"
		if len(title) < 2:
			raise ValidationError('Invalid {}. min is 2 character'.format(self.title))
		if len(title) > 40:
			raise ValidationError('Invalid {}, max is 40 character'.format(self.title))
		if  re.match(pattern, title) is None:
			raise ValidationError('Invalid {}. only alphanumeric is allowed'.format(self.title))
	#end def

	@validates('description')
	def validate_options(self, description):
	
		pattern = r"."
		if len(description) < 2:
			raise ValidationError('Invalid description, min is 2 characters')
		if re.match(pattern, description) is None:
			raise ValidationError('Invalid description')


class UpdateInfoSchema(Schema):
	title                  = fields.String(required=True, validate=cannot_be_blank)
	description            = fields.String(required=True, validate=cannot_be_blank)

	@validates('title')
	def validate_title(self, title):
		# only allow alphabet character and space
		pattern = r"."
		if len(title) < 2:
			raise ValidationError('Invalid email, min is 2 character')
		if len(title) > 40:
			raise ValidationError('Invalid email, max is 40 character')
		if  re.match(pattern, title) is None:
			raise ValidationError('Invalid creator, only Human allowed to create the field, not you')
	#end def

	@validates('description')
	def validate_description(self, description):
		# allow all characters except number
		pattern = r"."
		if len(description) < 2:
			raise ValidationError('Invalid description, min is 2 characters')
		if re.match(pattern, description) is None:
			raise ValidationError('invalid description')
	#end def
#end class

class TitleInfoSchema(Schema):
	title                  = fields.String(required=True, validate=cannot_be_blank)

	@validates('title')
	def validate_email(self, title):
		# only allow alphabet character and space
		pattern = r"."
		if len(title) < 2:
			raise ValidationError('Invalid title, min is 2 character')
		if  re.match(pattern, title) is None:
			raise ValidationError('Invalid title')
	#end def


