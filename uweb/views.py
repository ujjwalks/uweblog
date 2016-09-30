from django.views import generic
import requests
from django.http import HttpResponse


class HomePage(generic.TemplateView):
    template_name = "hello.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')