from wtforms import Form, BooleanField, \
	StringField, PasswordField, validators
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
	first_name = StringField('first_name', [validators.Length(min=4, max=50)])
	last_name = StringField('Username', [validators.Length(min=4, max=25)])

	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [
		validators.DataRequired(), 
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])	


# companyname = StringField('Company Name',
#                               validators=[InputRequired(),
#                                           Length(min=3, max=50)])
#     firstname = StringField('First Name',
#                             validators=[InputRequired(),
#                                         Length(min=2, max=50)])
#     surname = StringField('Surname',
#                           validators=[InputRequired(),
#                                       Length(min=2, max=50)])
#     username = StringField('Username',
#                            validators=[InputRequired(),
#                                        Length(min=4, max=25)])
#     email = StringField('Email',
#                         validators=[InputRequired(),
#                                     Email(message='Invalid Email'),
#                                     Length(min=6, max=50)])
#     password = PasswordField('Password',
#                              validators=[InputRequired(), Length(min=6)])