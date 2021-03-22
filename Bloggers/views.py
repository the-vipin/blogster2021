from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
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
from . models import Blogger
from .forms import manage_blogger_seo
from BlogPost.models import Blog
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from blogster.settings import metadatajson, metadataformjson
import json

# Create your views here.
class Bloggerlist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    
class myblocchannellist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    template_name = 'new_temp/pages/myblogchannel.html'
    
    def get_context_data(self, **kwargs):
        context = super(myblocchannellist, self).get_context_data(**kwargs)
        blogpages = Blogger.objects.filter(Q(Members=self.request.user) |Q(Founder=self.request.user))
        context['blogpages'] = blogpages
        return context



class subscribedBloggerlist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    template_name = 'Bloggers/listofSubscribedbloggers.html'

    def get_context_data(self, **kwargs):
        context = super(subscribedBloggerlist, self).get_context_data(**kwargs)
        context['bloggers'] = Blogger.objects.all()
        return context

class DashboardSettings(LoginRequiredMixin,UserPassesTestMixin,DetailView):
#class BloggerDashboard(DetailView):
    model = Blogger
    template_name = 'new_temp/dashboard/dashboardsetting.html'
    login_url = 'sign-in'

    def get_context_data(self, **kwargs):
        context = super(DashboardSettings, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        context['Members'] = User.objects.all()
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger))
        context['TITLE'] = 'dashboard ' + Blogger.BloggerName
        return context
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

class BloggerDashboard(LoginRequiredMixin,UserPassesTestMixin,DetailView):
#class BloggerDashboard(DetailView):
    model = Blogger
    template_name = 'new_temp/dashboard/dashboard.html'
    login_url = 'sign-in'

    def get_context_data(self, **kwargs):
        context = super(BloggerDashboard, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        context['Members'] = User.objects.all()
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger))
        context['TITLE'] = 'dashboard ' + Blogger.BloggerName
        return context
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

class BloggerView(DetailView):
    model = Blogger
    template_name = 'new_temp/pages/bloggerchhannel.html'

    def get_context_data(self, **kwargs):
        context = super(BloggerView, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        #context['Members'] = User.objects.all()
      #  context['meta'] = [x for x in metadatajson if(x['VIEW'] == 'viewblogger')],
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger),Q(ReadyToShow=True)).order_by('-created')
        context['TITLE'] = Blogger.BloggerName+'  - Blogster.co.in'
        context['description'] = Blogger.About + ' founded by '+ Blogger.Founder.username
        return context
    
class BloggerCreate(LoginRequiredMixin, CreateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['image','BloggerName','Accounttype']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        instances.Founder = self.request.user
        instances = form.save(commit=True)
        instances.Members.add(self.request.user)
        #instances.Members.add(self.request.user)
        #directory =  instances.BloggerName
        #os.mkdir(os.path.join(BASE_DIR, 'templates/bloggersbox/%s' % directory ))
        #os.mkdir(os.path.join(BASE_DIR, 'static/bloggersbox/%s' % directory ))
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(BloggerCreate, self).get_context_data(**kwargs)
        context['TITLE'] = 'Blogger creation form'
        context['formtype'] = 'Bloggercreation'
        context['submit_button_name'] = 'Create'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'sign up in blogster and join the community of innovative and revulationary minds. explore your mind. expand your reading. expand your knowledge'
        return context

class UpdateBlogger(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['image','BloggerName','About','Accounttype']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        instances.Founder = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(UpdateBlogger, self).get_context_data(**kwargs)
        context['TITLE'] = 'Update blogger details'
        context['formtype'] = 'Bloggerupdate'
        context['submit_button_name'] = 'Save details'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'sign up in blogster and join the community of innovative and revulationary minds. explore your mind. expand your reading. expand your knowledge'
        return context
        

class Update_Blogger_SE0(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blogger
    template_name =  'new_temp/form/seoform.html'
    login_url = 'sign-in'
    form_class = manage_blogger_seo
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(Update_Blogger_SE0, self).get_context_data(**kwargs)
        context['TITLE'] = 'Update SEO details of your channel'
        context['formtype'] = 'update_sml_channel'
        context['submit_button_name'] = 'Save SEO'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'add social media link in your channel so your audience can connet you at everywhere'
        return context
        
class Update_social_media_urls(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['facebook_url','instagram_url','youtube_url','twitter_url','snaptube_url','pinterest_url','tumblr_url']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(Update_social_media_urls, self).get_context_data(**kwargs)
        context['TITLE'] = 'Update social media links'
        context['formtype'] = 'update_sml_channel'
        context['submit_button_name'] = 'Update links'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'add social media link in your channel so your audience can connet you at everywhere'
        return context

class Update_personal_website_link(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['personal_websitelink']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user in Blogger.Members.all():
            return True
        elif self.request.user in Blogger.Founder:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(Update_personal_website_link, self).get_context_data(**kwargs)
        context['meta'] = [x for x in metadatajson if(x['VIEW'] == 'Update_personal_website_link')]
        context['TITLE'] = 'Update personal links'
        context['formtype'] = 'update_sml_channel'
        context['submit_button_name'] = 'Update links'
        return context

class DeleteBlogger(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blogger
    template_name =  'new_temp/dashboard/deleteblogger.html'
    login_url = 'sign-in'
    success_url = '/'

    def test_func(self):
        Blogger = self.get_object()
        if self.request.user == Blogger.Founder:
            return True
        return False

class BloggersubscribersToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blogger, slug=slug)
        url_ = blog.get_bloggerview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.subscribers.all():
                blog.subscribers.remove(user)
            else:
                blog.subscribers.add(user)
        return url_