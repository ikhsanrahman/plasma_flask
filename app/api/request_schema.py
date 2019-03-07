"""
    REQUEST SCHEMA
"""
#pylint: disable=too-few-public-methods
#pylint: disable=bad-whitespace
#pylint: disable=import-error

from flask_restplus import reqparse

class RegisterUserRequestSchema:
    """Define all mandatory argument for creating User"""
    parser = reqparse.RequestParser()
    parser.add_argument("name",    				type=str, required=True)
    parser.add_argument("email",        		type=str, required=True)
    parser.add_argument("password",   			type=str, required=True)
#end class

class UpdateUserRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("name",    				type=str, required=True)
	parser.add_argument("email",        		type=str, required=True)
	parser.add_argument("password",   			type=str, required=True)
	parser.add_argument("phone_number",			type=str, required=True)
	parser.add_argument("occupation",       	type=str, required=True)
	parser.add_argument("alamat",    			type=str, required=True)
	parser.add_argument("interesting_field",    type=str, required=True)

class LoginUserRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("email",        		type=str, required=True)
	parser.add_argument("password",   			type=str, required=True)


class VideoUserRequestSchema:
    """Define all mandatory argument for updating User"""
    parser = reqparse.RequestParser()
    parser.add_argument("judul_video",        	type=str, required=True)
    parser.add_argument("description",   		type=str, required=True)
    parser.add_argument("video",				type=str, required=True)
#end class

class PaperUserRequestSchema:
    """Define all mandatory argument for creating bank account"""
    parser = reqparse.RequestParser()
    parser.add_argument("judul_paper",			type=str, required=True)
    parser.add_argument("description",    		type=str, required=True)
#end class

class StoryUserRequestSchema:
    """Define all mandatory argument for authentication"""
    parser = reqparse.RequestParser()
    parser.add_argument("judul", 				type=str, required=True)
    parser.add_argument("content", 				type=str, required=True)
    parser.add_argument("penutup",				type=str)
#end class
