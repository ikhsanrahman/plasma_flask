
from flask import jsonify
from werkzeug.utils import secure_filename
import os

from app.api.create_app import db 
from app.api.db_model import Admin, File
from app.api.file.serializer import FileSchema

from app.api.config.config import Config

TIME = Config.time()
VIDEO_FOLDER = Config.VIDEO_FOLDER
PAPER_FOLDER = Config.PAPER_FOLDER


PAPER_ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc'])
VIDEO_ALLOWED_EXTENSIONS = set(['mp4', 'mpeg', '3gp', 'webm', 'avi', 'mov', 'flv', 'wmv'])



def allowed_file_paper(filename):
	allowed = '.' in filename and filename.rsplit('.', 1)[1].lower() in PAPER_ALLOWED_EXTENSIONS
	if allowed is True:
		return True
	else :
		return "extension paper is not allowed. the allowed file only .txt, .pdf, .doc"


def allowed_file_video(filename):
	allowed = '.' in filename and filename.rsplit('.', 1)[1].lower() in VIDEO_ALLOWED_EXTENSIONS
	if allowed is True:
 		return True
	else:
		return "extension file is not allowed. only extension .mp4, .mpeg, .3gp, .webm, .avi, .mov, .flv" 

class FileProcess:


	def upload_file(self, payload, admin_key):
		responses = {}
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		if not admin:
			return " no access"

		if 'name_file_video' not in payload:
			return "no video uploaded"

		if 'name_file_paper' not in payload:
			return "no paper uploaded"

		file_video = payload['name_file_video']
		file_paper = payload['name_file_paper']

		if file_video and allowed_file_video(file_video.filename):
			filename_video = secure_filename(file_video.filename)
			file_video.save(os.path.join(VIDEO_FOLDER, filename_video))

		if file_paper and allowed_file_paper(file_paper.filename):
			filename_paper = secure_filename(file_paper.filename)
			file_paper.save(os.path.join(PAPER_FOLDER, filename_paper))

		file = File.query.filter_by(title=payload['title']).first()

		if not file :
			new_file = File(title=payload['title'], name_file_video=filename_video, \
								name_file_paper=filename_paper, description=payload['description'], admin_id=admin.id )
			db.session.add(new_file)
			db.session.commit()
			return "upload file success"

		if not file :
			return "file already exist"
		


	def update_file(self, payload, admin_key, file_id):
		responses = {}
		file = File.query.get(file_id)
		admin = Admin.query.filter_by(admin_key=admin_key).first()		

		if file :
			if file.admin_id == admin.id is None:
				return "not access given"

			file.title = payload['title']
			file.description = payload['description']
			
			file.updated_at(TIME)
			db.session.commit()
			return "update file success"

		if not file:
			return "not file available "

	def remove_file(self, admin_key, file_id):
		responses = {}
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		file = File.query.get(file_id)
		print(file)
		if file:
			

			for x in os.listdir(os.chdir("/home/ikhsan/git/plasma_web_static/plasma_lab/data_paper")):
				if file.name_file_paper == x :
					os.remove(x)

			for x in os.listdir(os.chdir("/home/ikhsan/git/plasma_web_static/plasma_lab/data_video")):
				if file.name_file_video == x :
					os.remove(x)

			db.session.delete(file)
			db.session.commit()
			return "delete success"
		if not file:
			return "no file available"

	def get_files(self, admin_key):
		admin = Admin.query.filter_by(admin_key=admin_key).first()

		
		if admin:
			files = admin.files
			result = FileSchema(many=True).dump(files).data
			if result :
				return jsonify(result)

			if not result:
				return "no file available"
		if not admin:
			return "no access"

	def unactivate_file(self, admin_key, file_id):
		responses = {}

		admin = Admin.query.filter_by(admin_key=admin_key).first()
		file = File.query.filter_by(id=file_id).first()
		if admin :
			if file :
				if file.admin_id != admin.id:
					return "not access given"
				if file.status == False:
					return "file already unactive"
				if file.status == True:
					file.status = False
					db.session.commit()
					return "unactivate file has succeed"
			if not file:
				return "file is not available"
		if not admin:
			return "you don't have any access for this page"

	def reactivate_file(self, admin_key, file_id):
		responses = {}

		admin = Admin.query.filter_by(admin_key=admin_key).first()
		file = File.query.filter_by(id=file_id).first()
		if admin :
			if file :
				if file.admin_id != admin.id:
					return "not access given "
				if file.status == True:
					return "file already active"
				if file.status == False:
					file.status = True
					db.session.commit()
					return "reactivate file has succeed"
			if not file:
				return "file is not available"
		if not admin:
			return "you don't have any access for this page"


	def search_file_by_title(self, admin_key, payload):
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		files = File.query.all()
		output = []
		if admin :
			# if file.admin_id != admin_id:
			# 	return "not access given"
			for file in files :
				if payload['title'] in file.title:
					result = FileSchema().dump(file).data
					output.append(result)
				else :
					return "no file with {} available".format(payload['title'])
		if not admin:
			return "you don't have any access for this page"
		
		return output

	def search_file_by_name_file_paper(self, admin_key, payload):
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		files = File.query.all()
		output = []
		if admin :
			for file in files :
				if payload['name_file_paper'] in file.name_file_paper:
					result = FileSchema().dump(file).data
					output.append(result)
				else :
					return "no file with {} available".format(payload['name_file_paper'])

		if not admin:
			return "you don't have any access for this page"
		return output

	def search_file_by_name_file_video(self, admin_key, payload):
		admin = Admin.query.filter_by(admin_key=admin_key).first()
		files = File.query.all()
		output = []

		if admin :
			

			for file in files :
				if payload['name_file_video'] in file.name_file_video:
					result = FileSchema().dump(file).data
					output.append(result)
				else :
					return "no file with {} available".format(payload['name_file_video'])
		if not admin:
			return "you don't have any access for this page"
		return output
