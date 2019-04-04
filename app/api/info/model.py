from app.api.create_app import db 
from app.api.db_model import  Info, Admin
from app.api.info.serializer import *
from app.api.config.config import Config
from app.api.create_app import db

from flask import jsonify
 
from werkzeug.utils import secure_filename
import os

TIME = Config.time()
INFO_FOLDER = Config.INFO_FOLDER

RANDOM_FILE = set(['txt', 'pdf', 'doc', 'mp4', 'mpeg', '3gp', 'webm', 'avi', 'mov'])


class Info:

    def get_infos(self, admin_key):
		admin = Admin.query.get(admin_key)
		infos = admin.infos

		result = InfoSchema(many=True).dump(files).data

		if result :
			return jsonify(result)

		if not result:
			return "no info available"

			

	def upload_info(self, payload, admin_key):
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		responses = {}


		file_1 = payload['name_file_1']
		file_2 = payload['name_file_2']

		if file_1 and allowed_file_random(file_1.filename):
			filename_1 = secure_filename(file_1.filename)
			file_1.save(os.path.join(INFO_FOLDER, filename_info))

		if file_2 and allowed_file_paper(file_2.filename):
			filename_2 = secure_filename(file_2.filename)
			file_2.save(os.path.join(INFO_FOLDER, filename_2))

		file = File.query.filter_by(title=payload['title']).first()

		if not file :
			new_info = Info(title=payload['title'], name_file_1=filename_1, \
								name_file_2=filename_2, description=payload['description'], admin_id=admin.id )
			db.session.add(new_info)
			db.session.commit()
			return "upload info success"

		if not file :
			return "info already exist"

	def update_info(self, payload, admin_key, info_id):
		responses = {}
		info = Info.query.get(info_id)
		admin = Admin.query.filter_by(admin_key=admin_key).first()		

		if info :
			if info.admin_id == admin.id is None:
				return "not access given"

			info.title = payload['title']
			info.description = payload['description']
			
			info.updated_at(TIME)
			db.session.commit()
			return "update info success"

		if not file:
			return "not info available "

	def remove_info(self, admin_key, info_id):
		responses = {}
		info = Info.query.get(info_id)
		admin = Admin.query.filter_by(admin_key=admin_key).first()

		if info:
			if info.admin_id != admin.admin_id:
				return "not access given"
			db.session.delete(info)
			db.session.commit()

		if not info :
			return "no info can be deleted"

	def search_info_by_title(self, admin_key, payload):
		responses = {}
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		info = Info.query.all()
		result = []
		for x in info:
			if payload['title'] in x.full_name:
				info = InfoSchema().dump(x).data
				result.append(info)
			else :
				return "no info"
		if not result:
			return "no info detected"
		return result
