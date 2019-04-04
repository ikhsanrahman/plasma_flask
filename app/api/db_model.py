
import datetime
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


from app.api.create_app import db 
from app.api.config.config import Config 

TIME = Config.time()

class Admin(db.Model):
    __tablename__ = "admin"
    
    id                      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_key               = db.Column(db.String(255), default="2019")
    name                    = db.Column(db.String(255), unique=True)
    password                = db.Column(db.String(255), unique=True)
    password_hash           = db.Column(db.String(255), unique=True)
    files                   = db.relationship('File', backref='owner', cascade="delete", lazy=True)
    infos                   = db.relationship('Info', backref='owner', cascade="delete", lazy=True)

    def set_password(self, password):
        self.password = password

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__ (self):
        return '< This admin is {} >'.format(self.name)

class Info(db.Model):
    __tablename__='info'

    id                          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title                       = db.Column(db.Text)
    description                 = db.Column(db.Text)
    status                      = db.Column(db.Boolean, default=True)
    name_file_1                 = db.Column(db.String(255))
    name_file_2                 = db.Column(db.String(255))
    created_at                  = db.Column(db.DateTime, default=TIME)
    updated_at                  = db.Column(db.DateTime, default=TIME)
    deleted_at                  = db.Column(db.DateTime, default=TIME)
    admin_id                    = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    def status (self, status):
        self.status = status

    def created_at(self):
        self.time_created = TIME

    def updated_at(self) :
        self.time_updated = TIME

    def deleted_at(self):
        self.time_deleted = TIME

    def __repr__(self):
        return '< This event has title {} >'.format(self.title)

class File(db.Model):
    __tablename__ = 'file'
   
    id                           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title                        = db.Column(db.String(255))
    name_file_paper              = db.Column(db.String(255))
    name_file_video              = db.Column(db.String(255))
    description                  = db.Column(db.Text)
    status                       = db.Column(db.Boolean, default=True)
    like                         = db.Column(db.Integer, default=0)
    dislike                      = db.Column(db.Integer, default=0)
    time_updated                 = db.Column(db.DateTime)
    time_created                 = db.Column(db.DateTime, default=TIME)
    time_deleted                 = db.Column(db.DateTime)
    admin_id                     = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)


    def set_status(self, status):
        self.status = status

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_like_increment(self):
        self.like += 1

    def set_dislike_decrement(self):
        self.dislike += 1

    def created_at(self, TIME):
        self.time_created = TIME

    def updated_at(self, TIME) :
        self.time_updated = TIME

    def deleted_at(self, TIME):
        self.time_deleted = TIME
        
    def __repr__(self):
        return '< This video  with title {} belongs to {} >'.format(self.title, self.admin_id)



# class User(db.Model):
#     __tablename__ = 'users'

    
#     id          	           = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     full_name                  = db.Column(db.String(255))
#     email       	           = db.Column(db.String(255), unique=True)
#     password    	           = db.Column(db.String(255), unique=True)
#     password_hash              = db.Column(db.String(255), unique=True)
#     phone_number    	       = db.Column(db.String(255))
#     gender                     = db.Column(db.String(255))
#     category            	   = db.Column(db.String(255))
#     jurusan                    = db.Column(db.String(255))
#     universitas                = db.Column(db.String(255))
#     alamat                     = db.Column(db.String(255))
    
#     status                     = db.Column(db.Boolean, default=True)
#     time_created_user          = db.Column(db.DateTime, default=TIME)
#     time_updated_user          = db.Column(db.DateTime, default=None)
#     time_updated_pass          = db.Column(db.DateTime, default=None)
#     time_deleted               = db.Column(db.DateTime, default=None)
#     files                      = db.relationship('File', backref='owner', cascade="delete", lazy=True)
#     comments                   = db.relationship('Comment', backref='owner', lazy=True)
    

#     def set_full_name(self, full_name):
#         self.full_name = full_name

#     def set_password(self, password):
#         self.password = password

#     def set_password_hash(self, password) :
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password) :
#         return check_password_hash(self.password_hash, password)

#     def set_phone_number(self, phone_number):
#         self.phone_number = phone_number  

#     def set_alamat(self, alamat):
#         self.alamat = alamat

#     def set_category(self, category):
#         self.category = category

#     def set_jurusan(self, jurusan):
#         self.jurusan = jurusan

#     def set_universitas(self, universitas):
#         self.universitas = universitas

#     def is_authenticated(self):
#         return True

#     def is_anonymous(self):
#         return True 

#     def is_active (self):
#         self.status = True

#     def get_id(self):
#         return str(self.id)

#     def set_time_create_user(self, TIME):
#         self.time_created_user = TIME

#     def set_time_update_user(self, TIME) :
#         self.time_updated_user = TIME

#     def set_time_update_pass(self,TIME):
#         self.time_updated_pass = TIME 

#     def set_time_delete_user(self, TIME):
#         self.time_deleted = TIME

#     def __repr__(self):
#         return '< This user is {} and the id is {} >'.format(self.full_name, self.id)

#     end def
# end class



# class Story(db.Model):
#     __tablename__ = 'story'

    
#     id                          = db.Column(db.Integer, primary_key=True)
#     title                       = db.Column(db.Text)
#     description                 = db.Column(db.Text)
#     status                      = db.Column(db.Boolean, default=True)
#     created_at                  = db.Column(db.DateTime, default=TIME)
#     updated_at                  = db.Column(db.DateTime, default=TIME)
#     deleted_at                  = db.Column(db.DateTime, default=TIME)
#     user_id                     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False

#     def status (self, status_paper):
#         self.status = status

#     def created_at(self):
#         self.time_created = TIME

#     def updated_at(self) :
#         self.time_updated = TIME

#     def deleted_at(self):
#         self.time_deleted = TIME

#     def __repr__(self):
#         return '< This paper with title {} belongs to {} >'.format(self.judul_paper, self.owner)
    #end def
#end class

# class Description(db.Model):
#     __tablename__ = 'descriptions'
 
#     id                          = db.Column(db.Integer, primary_key=True)
#     description                 = db.Column(db.Text)
#     status                      = db.Column(db.Boolean, default=True)
#     videos                      = db.relationship('Video', backref='video', lazy=True)
#     papers                      = db.relationship('Paper', backref='paper', lazy=True)

#     def set_description(self, status):
#         self.status_description = status

#     def __repr__(self):
#         return "<this description {} explains about video and paper>".format(self.id)

