from app.api.db_model import Admin

from app.api.config.config import Config


TIME = Config.time()

print(Admin)

class AdminProcess:


	def login(self, payload, admin_key):
		responses = {}
		
		new_admin = Admin.query.filter_by(name=payload['name']).first()

		if new_admin.admin_key != admin_key:
			return "can not access"
		
		if not new_admin:
			return "no access given access at all"
		if new_admin.password != payload['password']:
			return "no access given"

		if new_admin and new_admin.check_password(payload['password']):
			return "login success"

		if not new_admin :
			return "you don't have any access at all"


	# def list_user(self, admin_key):
	# 	responses = {}

	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin:
	# 		users = User.query.all()
	# 		result = UserSchema(many=True).dump(users).data
	# 		if users :
	# 			return jsonify(result)

	# 		if not users:
	# 			return "no users available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def unactivate_user(self, admin_key, user_id):

	# 	responses = {}
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin:
	# 		user = User.query.filter_by(id=user_id).first()
	# 		if user:
	# 			if user.status == False:
	# 				return "user already unactivate"

	# 			if user.status == True:
	# 				user.status = False
	# 				db.session.commit()
	# 				return "unactivate user has succeed"
	# 		if not user:
	# 			return "user is not available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def reactivate_user(self, admin_key, user_id):
	# 	responses = {}

	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin:
	# 		user = User.query.filter_by(id=user_id).first()
	# 		if user :
	# 			if user.status == True:
	# 				return "user already active"
	# 			if user.status == False:
	# 				user.status = True
	# 				db.session.commit()
	# 				return "reactivate user has succeed"
	# 		if not user:
	# 			return "user is not available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def unactivate_file(self, admin_key):
	# 	responses = {}

	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(id=file_id).first()
	# 		if file :
	# 			if file.status == False:
	# 				return "file already unactive"
	# 			if file.status == True:
	# 				file.status = False
	# 				db.session.commit()
	# 				return "unactivate file has succeed"
	# 		if not file:
	# 			return "file is not available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def reactivate_file(self, admin_key, file_id):
	# 	responses = {}

	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(id=file_id).first()
	# 		if file :
	# 			if file.status == True:
	# 				return "file already active"
	# 			if file.status == False:
	# 				file.status = True
	# 				db.session.commit()
	# 				return "reactivate file has succeed"
	# 		if not file:
	# 			return "file is not available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_file_by_id(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(id=payload['file_id']).first()
	# 		result = FileSchema(many=True).dump(file).data
	# 		if result:
	# 			return jsonify(result)

	# 		if not result:
	# 			return "not file available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_file_by_title(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(title=payload['title']).first()
	# 		result = FileSchema(many=True).dump(file).data
	# 		if result:
	# 			return jsonify(result)

	# 		if not result:
	# 			return "not file available"

	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_file_by_name_file_paper(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(name_file_paper=payload['name_file_paper']).first()
	# 		result = FileSchema(many=True).dump(file).data
	# 		if result:
	# 			return jsonify(result)

	# 		if not result:
	# 			return "not file available"

	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_file_by_name_file_video(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		file = PaperAndVideo.query.filter_by(name_file_video=payload['name_file_video'])
	# 		result = FileSchema(many=True).dump(file).data
	# 		if result:
	# 			return jsonify(result)

	# 		if not result:
	# 			return "not file available"
	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_user_by_id(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		user = User.query.filter_by(id=payload['user_id']).first()
	# 		result = UserSchema().dump(user).data
	# 		if user:
	# 			return jsonify(result)

	# 		if not user:
	# 			return "not user available"

	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def search_user_by_name(self, admin_key, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :
	# 		users = User.query.all()
	# 		result = []
	# 		for x in users :
	# 			if payload['name'] in x.full_name :
	# 				user = UserSchema().dump(x).data
	# 				result.append(user)
	# 			else :
	# 				return "No user"

	# 		if not result:
	# 			return "No user detected"

	# 		return result

	# 	if not admin:
	# 		return "you don't have any access for this page"

	# def remove_user(self, admin_key, user_id,payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :

	# 		user = User.query.filter_by(id=user_id).first()
	# 		if users :
	# 			db.session.delete(user)
	# 			db.session.commit()
	# 			return "user has been deleted"

	# 		if not users:
	# 			return "no user can not be deleted"
	# 	if not admin:
	# 		return "you don't have any access for this page"
	
	# def remove_file(self, admin_key, file_id, payload):
	# 	admin = Admin.query.filter_by(admin_key=admin_key).first()
	# 	if admin :

	# 		file = PaperAndVideo.query.filter_by(id=file_id).first()

	# 		if file :
	# 			db.session.delete(file)
	# 			dg.session.commit()
	# 			return "file has been deleted"

	# 		if not users:
	# 			return "no user can be deleted"
	# 	if not admin:
	# 		return "you don't have any access for this page"


