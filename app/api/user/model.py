from app.api.create_app import db 
from app.api.db_model import *
from app.api.user.serializer import UserSchema

from flask import jsonify

from app.api.config.config import Config

TIME = Config.time()
class UserProcess:


	def create_user(self, payload):
		responses = {}
		user = User.query.filter_by(email=payload['email']).first()
		if not user:

			new_user = User(full_name = payload['full_name'], email=payload['email'], password=payload['password'], \
							phone_number=payload['phone_number'], gender=payload['gender'], category=payload['category'],\
							jurusan=payload['jurusan'], universitas=payload['universitas'], alamat=payload['alamat'] )
			new_user.set_password_hash(payload['password'])
			db.session.add(new_user)
			db.session.commit()
			return "register success"
		if user :
			return "User already existed"


	def update_user(self, payload, user_id):
		responses = {}
		user = User.query.filter_by(id=user_id).first()

		if user :
			user.full_name = payload['full_name']
			user.phone_number = payload ['phone_number']
			user.gender	= payload['gender']
			user.category = payload['commitategory']
			user.jurusan = payload['jurusan']
			user.universitas = payload['universitas']
			user.alamat = payload['alamat']
			user.set_time_update_user(TIME)
			db.session.commit()
			return "success"

		if not user:
			return "not available user"

	def update_password_user(self, payload, user_id):
		responses = {}
		user = User.query.filter_by(id=user_id).first()

		if user:
			user.set_password(payload['new_password'])
			user.set_password_hash(payload['new_password'])
			user.set_time_update_pass(TIME)
			db.session.commit()
			return "edit password success"
		if not user:
			return "edit password wrong"


	def login(self, payload):
		responses = {}
		user= User.query.filter_by(email=payload['email']).first()

		if user and user.check_password(payload['password']) is True:
			return "login success"
		
		
		return "login failed"

	# def unactivate_user(self, user_id):
	# 	user = User.query.filter_by(id=user_id).first()
	# 	if user :
	# 		user.status = False
	# 		db.session.commit()
	# 		return "delete user success"
	# 	if not user :
	# 		return "no user can be deleted"

	# def reactivate_user(self, user_id):
	# 	user = User.query.filter_by(id=user_id).first()
	# 	if user :
	# 		if user.status == True:
	# 			return "user already active"
	# 		if user.status == False:
	# 			user.status = True
	# 			db.session.commit()
	# 			return "reactivate user has succeed"
	# 	if not user:
	# 		return "user is not available"

	# def search_user_by_id(self, user_id):
	# 	user = User.query.filter_by(id=user_id).first()
	# 	result = UserSchema().dump(user).data
	# 	if user:
	# 		return jsonify(result)

	# 	if not user:
	# 		return "not user available"

	# def search_user_by_name(self, payload):
	# 	users = User.query.all()
	# 	result = []
	# 	for x in users :
	# 		if payload['name'] in x.full_name :
	# 			user = UserSchema().dump(x).data
	# 			result.append(user)
	# 		else :
	# 			return "No user"

	# 	if not result:
	# 		return "No user detected"

	# 	return result

	# def get_users(self):
	# 	users = User.query.filter_by(status=True).all()
	# 	result = UserSchema(many=True).dump(users).data
	# 	if users :
	# 		return jsonify(result)

	# 	if not users:
	# 		return "no users available"

