
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from infodata.models import HelpCenter
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, RedirectView


def homepage(request):
    return render(request,'staffcontrol/homepage.html')


class helpcenterpage(ListView):
    model = HelpCenter
    template_name = 'staffcontrol/helpcenter/helpcenterpage.html'

class create_article_for_helpcenterpage(CreateView):
    model = HelpCenter
    template_name = 'staffcontrol/helpcenter/create_article.html'
    login_url = 'sign-in'
    fields = ['subject_name','Group','articalname','content']
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        return super().form_valid(form)

class Edit_artical(UpdateView):
    model = HelpCenter
    template_name = 'staffcontrol/helpcenter/create_article.html'
    login_url = 'sign-in'
    fields = ['subject_name','Group','articalname','content']
    success_url = '/'
    
    def form_valid(self, form, *args, **kwargs):
        return super().form_valid(form)

class Delete_artical(DeleteView):
    model = HelpCenter
    template_name =  'staffcontrol/delete.html'
    login_url = 'sign-in'
    success_url = '/'





