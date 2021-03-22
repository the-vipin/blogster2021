from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, RedirectView
from infodata.json import hc_json

# Create your views here.
from blogster.basicdata import domainname, domainname_fullurl
from infodata.models import HelpCenter

def textview(request):
    return HttpResponse('welcome jiii')

class helpcenterpage(ListView):
    model = HelpCenter
    template_name = 'infodata/helpHc.html'



class ArticleReadview(DetailView):
    model = HelpCenter
    template_name = 'staffcontrol/helpcenter/article.html'