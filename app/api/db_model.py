"""
	the module for saving a process that happen during sending sms 
	to sms gateway
	_____________________*********____________________________
"""

import datetime
from flask import jsonify
from app.api.create_app import db 
from app.api.config.config import Config 

TIME = Config.time()


class User(db.Model):
    __tablename__ = 'users'
    """
        This is class that represent a Table of Database to store process of sending OTP Code
        before and after sending to sms Gateway
    """
    id          	           = db.Column(db.Integer, primary_key=True)
    name                       = db.Column(db.String(255))
    email       	           = db.Column(db.String(255), unique=True)
    password    	           = db.Column(db.String(255), unique=True)
    occupation    	           = db.Column(db.String(255))
    phone_number    	       = db.Column(db.String(255))
    alamat      	           = db.Column(db.String(255))
    interesting_field    	   = db.Column(db.String(255))#respond from sms gateway
    status_user                = db.Column(db.Boolean(False))
    created_at  	           = db.Column(db.DateTime, default=TIME)
    updated_at                 = db.Column(db.DateTime, default=TIME)
    

    def __repr__(self):
        return '< This user is {} >'.format(self.name)

    def update(self) :
        self.updated_at = TIME
       

    def set_status_user(self, status):
        self.status_user = status

    #end def
#end class

class VideoUser(db.Model):
    __tablename__ = 'video_user'
    """
        This is class that represent a Table of Database to store entire process to verificate OTP Code
        before and after sending to Sms Gateway
    """
    id                           = db.Column(db.Integer, primary_key=True)
    judul_video                  = db.Column(db.String(255))
    name_video                   = db.Column(db.String(255))
    description                  = db.Column(db.String(255))
    updated_at                   = db.Column(db.DateTime, default=TIME)
    created_at                   = db.Column(db.DateTime, default=TIME)
    #owner                        = 

    def __repr__(self):
        return '< This video  with title {} belongs to {} >'.format(self.judul_video, self.owner)

    #end def
#end class

class PaperUser(db.Model):
    __tablename__ = 'paper_user'
    """
        This is class that represent Table of Database to Store process in single sms
        before and after sending to SMS gateway
    """
    id                          = db.Column(db.Integer, primary_key=True)
    judul_paper                 = db.Column(db.Text())
    name_paper                  = db.Column(db.String(255))
    description                 = db.Column(db.String(255))
    created_at                  = db.Column(db.DateTime, default=TIME)
    updated_at                  = db.Column(db.DateTime, default=TIME)
    #owner                       = db.
    
    def update(self):
        self.updated_at = TIME
    #end def

    def __repr__(self):
        return '< This paper with title {} belongs to {} >'.format(self.judul_paper, self.owner)
    #end def
#end class

class StoryUser(db.Model):
    __tablename__ = 'story_user'
    """
        This is class that represent a Table of Database to store a process in Single 
        Custom Sms before and after sending to Sms Gateway
    """
    id                          = db.Column(db.Integer, primary_key=True)
    judul                       = db.Column(db.Text())
    content                     = db.Column(db.Text())
    penutup                     = db.Column(db.Text())
    created_at                  = db.Column(db.DateTime, default=TIME)
    updated_at                  = db.Column(db.DateTime, default=TIME)
    #owner                       = 
    
    def update(self):
        self.updated_at = TIME
    #end def

    def __repr__(self):
        return '< This story with title {} belongs to {} >'.format(self.judul, self.owner)
    #end def
#end class
