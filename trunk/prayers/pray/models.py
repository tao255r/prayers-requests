from django.db import models

from google.appengine.ext import db

class Visitor(db.Model):
    ip = db.StringProperty()
    user = db.StringProperty()
    added_on = db.DateTimeProperty(auto_now_add=True)
    
