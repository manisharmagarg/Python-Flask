from emailApp import *
# from emailApp.views.forms import RegistrationForm
from emailApp.views.baseview import BaseView
from emailApp.models import User
# from .models import User


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@login_manager.user_loader
def load_user(id):
    print '[%s]' % db.session.query(User).get(id)
    return db.session.query(User).get(id)

# @login_required
class HomeView(BaseView):

	def __init__(self):
		self.response = dict()
	@login_required
	def get(self):
		self.response['success'] = True
		self.response['message'] = 'Email App is Running'
		return jsonify(self.response)


class UserRegistration(BaseView):

	def __init__(self):
		self.context = dict()

	def get_template_name(self):
		return 'register.html'

	def get(self):
		return self.render_template(self.context)

	def post(self):
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		email = request.form.get('email')
		password = request.form.get('password')
		pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
		user = User(email=email, password=pw_hash,
			first_name=firstname, last_name=lastname)
		db.session.add(user)
		db.session.commit()
		return redirect('login')


class UserLogin(BaseView):

	def __init__(self):
		self.context = dict()

	def get_template_name(self):
		return 'login.html'

	def get(self):
		return self.render_template(self.context)

	def post(self):
		email = request.form.get('email')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()

		if user:
			if bool(bcrypt.check_password_hash(user.password, password)):
				login_user(user)
				return redirect("campaigns")
			else:
				self.context['msg'] = 'Invaild User and password'
		else:
			self.context['msg'] = "Invaild User"
		return self.render_template(self.context)


class UserLogout(BaseView):
	def __init__(self):
		pass
	@login_required
	def get(self):
		logout_user()
		return redirect('login')
