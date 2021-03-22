from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, RedirectView
from itertools import chain
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from .models import Blog
from Bloggers.models import Blogger
import urllib.request
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.conf import settings
from django.contrib.auth.decorators import login_required
from hitcount.views import HitCountDetailView
from django.utils.translation import gettext_lazy as _
from .forms import Commentform, blogcreationform, manage_blog_seo
from .models import Comments
from django.views.generic.edit import FormMixin
from django.urls import reverse

##
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import blogEditform

class blogCreate_view(LoginRequiredMixin, CreateView, FormMixin):
    model = Blog
    template_name =  'new_temp/blogpost/forms/blogCreate.html'
    login_url = 'sign-in'
    form_class = blogEditform
  #  form_class = blogcreationform
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        instances = form.save(commit=False)
        instances.Uploader = self.request.user
        slug = self.kwargs.get("slug")
        instances.BloggerAc = get_object_or_404(Blogger, slug=slug)
        return super().form_valid(form)
    
 #  def get_success_url(self):
  #      slug = self.kwargs["pk"]
   #     return reverse("createBlog", kwargs={'slug': slug})
    
    def get_context_data(self, **kwargs):
        context = super(blogCreate_view, self).get_context_data(**kwargs)
        context['TITLE'] = 'create blogpost'
        return context
    


class blogEdit_view(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name =  'new_temp/blogpost/forms/blogEdit.html'
    login_url = 'sign-in'
    form_class = blogEditform
    success_url = '/'
    
    @csrf_exempt
    def POST(self, form):
        if self.request.is_ajax():
            form = blogEditform(self.request.POST)
            if form.is_valid():
                text = form.save(commit=False)
                text.save()
                response = {'msg':'blog Saved'}
                return JsonResponse(response)
        response = {'msg':'failed to save blog'}
        return JsonResponse(response)
        
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False

