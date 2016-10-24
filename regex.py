import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

    

def valid_username(username):
    if(USER_RE.match(username)):
        return True

def valid_password(password):
    if(PASS_RE.match(password)):
        return True

def valid_email(email):
    if(EMAIL_RE.match(email)):
        return True

def same_password(password, verpassword):
    if(password == verpassword):
        return True
