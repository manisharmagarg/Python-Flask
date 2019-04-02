from emailApp import *
import uuid
import datetime
from sqlalchemy import Column, Integer, Text
from sqlalchemy import ForeignKey
# from sqlalchemy.dialects.postgresql import JSON, JSONB

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name, email, password):
    	self.first_name = first_name
    	self.last_name = last_name
    	self.email = email
    	self.password = password

    def __str__(self):
    	return self.email

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        	'id': self.id,
        	'first_name': self.first_name,
        	'last_name': self.last_name, 
        	'email': self.email, 
        	'password': self.password
        }

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
