from emailApp import app
from emailApp.views.accounts import HomeView, UserRegistration , UserLogin, UserLogout
from emailApp.views.campaigns import Campaigns

app.add_url_rule('/', view_func=HomeView.as_view('home'))

app.add_url_rule('/register/', view_func=UserRegistration.as_view('UserRegistration'))

app.add_url_rule('/login/', view_func=UserLogin.as_view('login'))

app.add_url_rule('/logout/', view_func=UserLogout.as_view('logout'))

app.add_url_rule('/campaigns/', view_func=Campaigns.as_view('campaigns'))