
import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.file.serializer import *
from app.api.file.model import FileProcess
from app.api.request_schema import *

from app.api.config import config

from app.api.namespace import Video

api = Video.api


@api.route('/<string:admin_key>/admin/file')
class UploadFile(Resource):

    @api.doc('get list file')
    def get(self, admin_key):
        result = FileProcess().get_files(admin_key)
        return result

    @api.doc('upload file')
    def post(self, admin_key):
        
        payload = FileRequestSchema().parser.parse_args(strict=True)

        errors = FileSchema().load(payload).errors
        if errors :
            return errors

        result = FileProcess().upload_file(payload, admin_key)
        return result
    #end def

   
@api.route('/<string:admin_key>/admin/<int:file_id>/file/update')
class UpdateFile(Resource):
    
    @api.doc('update a file')
    def put(self, admin_key, file_id):
       
        payload = UpdateFileRequestSchema().parser.parse_args(strict=True)

        errors = UpdateFileSchema().load(payload).errors
    
        if errors :
            return errors
        
        update_file = FileProcess().update_file(payload, admin_key, file_id)
        return update_file
    #end def

@api.route('/<string:admin_key>/admin/<int:file_id>/file/remove')
class RemoveFile(Resource):
    
    @api.doc('remove file')
    def delete(self, admin_key, file_id):
       

        delete_file = FileProcess().remove_file(admin_key, file_id)
        return delete_file
    #end def

@api.route('/<string:admin_key>/admin/<int:file_id>/file/unactivate')
class UnactivateFile(Resource):

    @api.doc('unactivate file')
    def delete(self, admin_key, file_id):
        result = FileProcess().unactivate_file(admin_key, file_id)
        return result

@api.route('/<string:admin_key>/admin/<int:file_id>/file/reactivate')
class ReactivateFile(Resource):

    @api.doc('reactivate file')
    def get(self, admin_key, file_id):
        
        result = FileProcess().reactivate_file(admin_key, file_id)
        return result
    #end def

   
@api.route('/<string:admin_key>/admin/file/title')
class SearchFileByTitle(Resource):
    
    @api.doc('search by title')
    def get(self, admin_key):
       
        payload = TitleFileRequestSchema().parser.parse_args(strict=True)
        print(payload)
        errors = TitleFileSchema().load(payload).errors
    
        if errors :
            return errors
        
        search_by_title = FileProcess().search_file_by_title(admin_key, payload )
        return search_by_title
    #end def

@api.route('/<string:admin_key>/admin/file/paper')
class SearchByNamePaper(Resource):
    
    @api.doc('search by name paper')
    def get(self, admin_key):
       
        payload = PaperFileRequestSchema().parser.parse_args(strict=True)

        errors = PaperFileSchema().load(payload).errors
    
        if errors :
            return errors
        
        search_by_name_paper = FileProcess().search_file_by_name_file_paper(admin_key, payload)
        return search_by_name_paper
    #end def

@api.route('/<string:admin_key>/admin/file/video')
class SearchByNameVideo(Resource):
    
    @api.doc('remove by name paper')
    def get(self, admin_key):
       
        payload = VideoFileRequestSchema().parser.parse_args(strict=True)

        errors = VideoFileSchema().load(payload).errors
    
        if errors :
            return errors
        
        search_by_name_video = FileProcess().search_file_by_name_file_video(admin_key, payload)
        return search_by_name_video
    #end def




