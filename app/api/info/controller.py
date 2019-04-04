
import datetime
import jwt

from flask import request, make_response, jsonify
from flask_restplus import Resource

from app.api.info.serializer import *
from app.api.file.model import FileProcess
from app.api.request_schema import *

from app.api.config import config

from app.api.namespace import Info

api = Info.api


@api.route('/<string:admin_key>/admin/info')
class UploadInfo(Resource):

    @api.doc('get list info')
    def get(self, admin_key):
        result = InfoProcess().get_infos(admin_key)
        return result

    @api.doc('upload info')
    def post(self, admin_key):
        
        payload = InfoRequestSchema().parser.parse_args(strict=True)

        errors = infoSchema().load(payload).errors
        if errors :
            return errors

        result = InfoProcess().upload_info(payload, admin_key)
        return result
    #end def

   
@api.route('/<string:admin_key>/admin/<int:info_id>/info/update')
class UpdateInfo(Resource):
    
    @api.doc('update a info')
    def put(self, admin_key, info_id):
       
        payload = UpdateInfoRequestSchema().parser.parse_args(strict=True)

        errors = UpdateInfoSchema().load(payload).errors
    
        if errors :
            return errors
        
        update_info = FileProcess().update_info(payload, admin_key, info_id)
        return update_info
    #end def

@api.route('/<string:admin_key>/admin/<int:info_id>/info/remove')
class RemoveInfo(Resource):
    
    @api.doc('remove info')
    def delete(self, admin_key, info_id):
       

        delete_info = InfoProcess().remove_info(admin_key, info_id)
        return delete_info
    #end def

   
@api.route('/<string:admin_key>/admin/info/title')
class SearchInfoByTitle(Resource):
    
    @api.doc('search by title')
    def get(self, admin_key):
       
        payload = TitleInfoRequestSchema().parser.parse_args(strict=True)

        errors = InfoFileSchema().load(payload).errors
    
        if errors :
            return errors
        
        search_by_title = InfoProcess().search_info_by_title(payload, admin_key)
        return search_by_title
    #end def





