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

# Create your views here.
class Bloglist(ListView):
    model = Blog

class BlogAnalyseView(DetailView):
    model = Blog
    template_name = 'new_temp/pages/blogAnalyseview.html'

class Blogview(HitCountDetailView, FormMixin):
    model = Blog
    template_name =  'new_temp/pages/blogpage.html'
    count_hit = True
    form_class = Commentform
    
    def get_success_url(self):
        return reverse('BlogPostview', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(Blogview, self).get_context_data(**kwargs)
        context['form'] = Commentform(initial={
            'Commenton': self.object,
            'Commentfrom': self.request.user
        })
        context['blogpost_comments'] = Blog.objects.annotate(total_comments = Count('Commenton'))
        context['comment_list'] = Comments.objects.filter(Q(Commenton_id=self.object.id))
        #context['comments'] = self.object.comment_set.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(Blogview, self).form_valid(form)
    
    

    

class BlogCreate(LoginRequiredMixin, CreateView, FormMixin):
    model = Blog
    template_name =  'blogs/blogtinyeditor.html'
    login_url = 'sign-in'
    fields = ['Blogtiltle','UpBlog']
  #  form_class = blogcreationform
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        instances = form.save(commit=False)
        instances.Uploader = self.request.user
        slug = self.kwargs.get("slug")
        instances.BloggerAc = get_object_or_404(Blogger, slug=slug)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(BlogCreate, self).get_context_data(**kwargs)
        context['TITLE'] = 'create blogpost'
        return context
        
class Manage_Blog_Seo(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name =  'new_temp/form/seoform.html'
    login_url = 'sign-in'
    form_class = manage_blog_seo
    success_url = '/'
    
    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(Manage_Blog_Seo, self).get_context_data(**kwargs)
        context['TITLE'] = 'Manage Blog Seo'
        context['formtype'] = 'updateblogdetails'
        context['submit_button_name'] = 'Save SEO'
        return context
        
    
class UpdateBlog(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name =  'new_temp/form/seoform.html'
    login_url = 'sign-in'
    fields = ['Blogtiltle','Discription','image','Conclusion']
    success_url = '/'
    
    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(UpdateBlog, self).get_context_data(**kwargs)
        context['TITLE'] = 'edit blog details'
        context['formtype'] = 'updateblogdetails'
        context['submit_button_name'] = 'Save'
        return context


class DeleteBlog(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    template_name =  'blogs/Deleteblog.html'
    login_url = 'sign-in'
    success_url = '/'

    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False


        
class BlogPostCommentOn(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'
    
    def post_comment(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        if request.method == 'POST':
            form = Commentform(request.POST)
            if form.is_valid():
                #Comment = form.cleaned_data['Comment']
                #blog.comments_set.create(Comment=Comment)
                instances = form.save(commit=False)
                instances.Commentfrom = self.request.user.id
                instances.Commenton = blog.id
                form.save()
                #messages.infos(request,comment)
        return url_

class BlogPostlikeToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.likes.all():
                blog.likes.remove(user)
            else:
                blog.likes.add(user)
                if user in blog.Dislikes.all():
                    blog.Dislikes.remove(user)
        return url_
        
class BlogPostDislikeToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.Dislikes.all():
                blog.Dislikes.remove(user)
            else:
                blog.Dislikes.add(user)
                if user in blog.likes.all():
                    blog.likes.remove(user)
        return url_
        
class BlogPostSaveToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.save_readlater.all():
                blog.save_readlater.remove(user)
            else:
                blog.save_readlater.add(user)
        return url_

class LikedBlogpost(LoginRequiredMixin, ListView):
    model = Blog 
    template_name = 'blogs/userlikedblogs.html'
    context_object_name = 'blogs'
    login_url = 'sign-in'

    def get_queryset(self):
        result = super(LikedBlogpost, self).get_queryset()
        query = self.request.user
        if query:    
            result = Blog.objects.filter(
                Q(likes=query) )
        else:
            result = None
        return result
        

class SavedBlogpost(LoginRequiredMixin, ListView):
    model = Blog 
    template_name = 'blogs/userlikedblogs.html'
    context_object_name = 'blogs'
    login_url = 'sign-in'

    def get_queryset(self):
        result = super(SavedBlogpost, self).get_queryset()
        query = self.request.user
        if query:    
            result = Blog.objects.filter(
                Q(save_readlater=query) )
        else:
            result = None
        return result
        
