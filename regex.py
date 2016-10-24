import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

    

def valid_username(self, username):
    if(USER_RE.match(self.username)):
        return True

def valid_password(self, password, verpassword):
    if(PASS_RE.match(self.password)):
        return True

def valid_email(self, email):
    if(EMAIL_RE.match(self.email)):
        return True

def same_password(self, password, verpassword):
    if(self.password == self.verpassword):
        return True
