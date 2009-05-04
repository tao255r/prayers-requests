from django.http import HttpResponse, HttpResponseForbidden
from google.appengine.api import users

from prayers.pray.models import Visitor

def index(request):
    
    user = users.GetCurrentUser()
    
    if user is None:
        login_link = users.CreateLoginURL(request.path)
        return HttpResponseForbidden('You must be signed in to <a href=%s>continue</a>. ' % login_link)
    
    visitor = Visitor()
    visitor.user = user.nickname()
    visitor.ip = request.META["REMOTE_ADDR"]
    visitor.put()
    
    result = ""
    visitors = Visitor.all()
    visitors.order("-added_on")
    
    for visitor in visitors.fetch(limit=40):
        result += visitor.user + '(' + visitor.ip + ')' + u" visited on " + unicode(visitor.added_on) + "<br>"
    
    return HttpResponse(result)