# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
#from pray.forms import UserRegistrationForm
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    (r'^powered/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'powered.html'}),
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'dashboard.html'}, name='Dashboard'),
    
) + urlpatterns
