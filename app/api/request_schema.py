"""
	REQUEST SCHEMA
"""
#pylint: disable=too-few-public-methods
#pylint: disable=bad-whitespace
#pylint: disable=import-error
from werkzeug.datastructures import FileStorage
from flask_restplus import reqparse

class UserRequestSchema:
	"""Define all mandatory argument for creating User"""
	parser = reqparse.RequestParser()
	parser.add_argument("full_name",    type=str, required=True)
	parser.add_argument("email",        type=str, required=True)
	parser.add_argument("password",   type=str, required=True)
	parser.add_argument("confirm_password", type=str, required=True)
	parser.add_argument("phone_number",type=str, required=True)
	parser.add_argument("gender", type=str)
	parser.add_argument("category",    type=str, required=True)
	parser.add_argument("jurusan",         type=str, required=True)
	parser.add_argument("universitas",        type=str, required=True)
	parser.add_argument("alamat",       type=str)
#end class

class LoginUserRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("email",    type=str, required=True)
	parser.add_argument("password",        type=str, required=True)

class UpdateUserRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("full_name",    type=str, required=True)
	parser.add_argument("phone_number",type=str, required=True)
	parser.add_argument("gender", type=str)
	parser.add_argument("category",    type=str, required=True)
	parser.add_argument("jurusan",         type=str, required=True)
	parser.add_argument("universitas",        type=str, required=True)
	parser.add_argument("alamat",       type=str)

class SearchUserRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("name",    type=str, required=True)


class UpdatePasswordRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("new_password",                type=str, required=True)
	parser.add_argument("confirm_new_password",        type=str, required=True)


#----------------------------------- FILE ------------------------------#

class FileRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)
	parser.add_argument("name_file_paper", type=FileStorage, location='files', required=True)
	parser.add_argument("name_file_video", type=FileStorage, location='files', required=True)
	parser.add_argument("description", type=str, required=True)

class UpdateFileRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)
	parser.add_argument("description", type=str, required=True)


class TitleFileRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)

class PaperFileRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("name_file_paper", type=str, required=True)

class VideoFileRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("name_file_video", type=str, required=True)

# ---------------------------------- ADMIN ------------------------------------#


class AdminRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("name", type=str, required=True)
	parser.add_argument("password", type=str, required=True)


#------------------------ INFO ------------------------------#

class InfoRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)
	parser.add_argument("name_file_1", type=FileStorage, location='files', required=True)
	parser.add_argument("name_file_2", type=FileStorage, location='files', required=True)
	parser.add_argument("description", type=str, required=True)

class UpdateInfoRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)
	parser.add_argument("description", type=str, required=True)

class TitleInfoRequestSchema:
	parser = reqparse.RequestParser()
	parser.add_argument("title", type=str, required=True)


