import os
import traceback
from datetime import datetime

# import Flask module
from flask import Flask, render_template, request, redirect, jsonify

# import flask manager
from flask_script import Manager

# import flask migrations
from flask_migrate import Migrate, MigrateCommand

# import flask sqlalachemy
from flask_sqlalchemy import SQLAlchemy

# bcrypt user password
from flask_bcrypt import Bcrypt

# create login required (flask decorator)
from flask_login import LoginManager, UserMixin, login_user, login_required, \
    logout_user, current_user


template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = \
		'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(
			user = os.environ.get('POSTGRES_USER', 'nessus'), 
			password = os.environ.get('POSTGRES_PASSWORD', '123'),
			host = os.environ.get('POSTGRES_HOST', 'localhost'), 
			port = os.environ.get('POSTGRES_PORT', '5432'), 
			db_name = os.environ.get('POSTGRES_DB', 'nessus_driver')
		)
# app.config['SQLALCHEMY_DATABASE_URI'] = \
	# "sqlite:///email_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = 'flask_login'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
