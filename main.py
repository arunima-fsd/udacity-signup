

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
        self.render("index.html", test1 = "autofocus")

    def post(self):
    	user = self.request.get("username")
    	password = self.request.get("password")
    	verpassword = self.request.get("verpassword")
    	email = self.request.get("email")

    	if(user):
    		if(regex.valid_username(user)):
    			if(password):
    				if(verpassword):
    					if(regex.valid_password(password)):
    						if(regex.same_password(password, verpassword)):
    							if(email):
    								if(regex.valid_email(email)):
    									self.redirect("/welcome?username=%s"%user)
    								else:
    									self.render("index.html", email_error_msg = "Invalid email address", user = user, test4= "autofocus")
    							else:
    								self.redirect("/welcome?username=%s"%user)
    						else:
    							self.render("index.html", pass_error_msg_2 = "Your passwords didn't match", user = user, test2 = "autofocus", email =email)
    					else:
    						self.render("index.html", pass_error_msg = "Invalid password", user = user, test2 = "autofocus", email = email)
    				else:
    					self.render("index.html", pass_error_msg_2 = "Please repeat the password", user = user, test2 = "autofocus", email = email)
    			else:
    				self.render("index.html", pass_error_msg = "Please enter password", user= user, test2 = "autofocus", email = email)
    		else:
    			self.render("index.html", user_error_msg = "Invalid username", test1 = "autofocus", email = email)
    	else:
    		self.render("index.html", user_error_msg = "Please enter user name", test1 = "autofocus", email = email)



class WelcomeHandler(Handler):
	def get(self):
		username = self.request.get("username")
		self.render("welcome.html", user = username)

    	
    	




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/welcome', WelcomeHandler)
], debug=True)
