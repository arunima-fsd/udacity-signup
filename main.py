

import webapp2

import os

import jinja2

import regex

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)




class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		


class MainPage(Handler):
    def get(self):
        self.render("index.html")

    def post(self):
    	user = self.request.get("username")
    	password = self.request.get("password")
    	verpassword = self.request.get("verpassword")
    	email = self.request.get("email")

    	if(user):
    		if(regex.valid_username(user)):
    			if(password and verpassword):
    				if(regex.valid_password(password)):
    					if(regex.match_password(password, verpassword)):
    						if(email):
    							if(regex.valid_email(email)):
    								self.render("welcome.html", user = user)
    							else:
    								self.render("index.html", email_error_msg = "Invalid email address")
    						else:
    							self.render("welcome.html", user = user)
    					else:
    						self.render("index.html", pass_error_msg_2 = "Your passwords didn't match")
    				else:
    					self.render("index.html", pass_error_msg_1 = "Invalid password")
    			else:
    				self.render("index.html", pass_error_msg_1 = "Please enter the password")
    		else:
    			self.render("index.html", user_error_msg = "Invalid username")
    	else:
    		self.render("index.html", user_error_msg = "Please enter user name")




    	
    	




app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
