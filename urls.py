# -*- coding: utf-8 -*- 
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
#from pray.forms import UserRegistrationForm
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    # Admin Interface
    ('^admin/(.*)', admin.site.root),
    
    # Powered Page
    (r'^powered/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'powered.html'}),
    
    # Dashboard Page
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'dashboard.html'}, name='Dashboard'),
    
    # Profile page
    (r'^profiles/', include('profiles.urls')),
    
    # Sample page
    (r'^sample/', 'django.views.generic.simple.direct_to_template',
        {'template': 'sample.html'}),
    
) + urlpatterns

# try google code online editor
