from google.appengine.ext import db
from django.contrib.auth.models import User
from django.db.models import permalink
from django.contrib import admin

class Prayerprofile(db.Model):
    """ User Profile model  """
    
    PRIVACY_LEVEL_CHOICES = (
        'Only myself',
        'Only friends',
        'In groups',
        'Public for everyone',
    )
    
    GENDER_NAME_CHOICES = (
        'Brother',
        'Sister',
    )
    
    user = db.ReferenceProperty(User, required=True)
    
    fname       = db.StringProperty()
    nickname    = db.StringProperty()
    gender      = db.StringProperty(choices=GENDER_NAME_CHOICES)
    bday        = db.DateProperty()
    location    = db.StringProperty()
    avatar      = db.BlobProperty()
    date_updated= db.DateProperty(auto_now=True)
    date_joined = db.DateProperty(auto_now_add=True)
    privacy     = db.StringProperty(choices=PRIVACY_LEVEL_CHOICES)
    latest_news = db.StringProperty(multiline=True)
    
    def __unicode__(self):
        return '%s(%s)' % (self.fname, self.nickname)
        
    @permalink
    def get_absolute_url(self):
        return ('profiles_prayerprofile_detail', (), { 'username': self.user.username })
        
        
class PrayerprofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fname', 'nickname', 'gender',
                    'bday', 'location', 'avatar', 'date_updated', 'date_joined', 'privacy')

admin.site.register(Prayerprofile, PrayerprofileAdmin)
        