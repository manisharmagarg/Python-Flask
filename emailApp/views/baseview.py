from emailApp import *
from flask.views import MethodView
from flask.views import View


class BaseView(MethodView):

	def get_template_name(self):
		raise NotImplementedError()

	def render_template(self, context):
		return render_template(self.get_template_name(), **context)
