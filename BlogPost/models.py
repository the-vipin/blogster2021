from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.db.models.signals import pre_save
from Bloggers.models import Blogger
import os
from django.urls import reverse
from django.contrib import admin
from django.utils import timezone
import datetime


from django.contrib.contenttypes.fields import GenericRelation
import six
from six import python_2_unicode_compatible

from django.utils.text import slugify
from functions.string_generator import random_digita_generator


class Blog(models.Model):
    Blogtiltle = models.CharField(max_length=60)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    Discription = models.CharField(max_length=160 , blank=True, null=True)
    BloggerAc = models.ForeignKey(Blogger,related_name='bloggerAc', on_delete=models.CASCADE)
    Authors = models.ManyToManyField(User, related_name='BlogMembers')
    Uploader = models.ForeignKey(User,related_name='bloguploader', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='BlogThumnailimg/' ,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blogpostLikes',blank=True)
    Dislikes = models.ManyToManyField(User, related_name='blogpostdislike',blank=True)
    save_readlater = models.ManyToManyField(User, related_name='blogpostreadlater',blank=True)
    UpBlog = models.TextField(blank=True, null=True)
    ReadyToShow = models.BooleanField(default=True)
    Conclusion = models.CharField(max_length=400, blank=True)
    Meta_discription = models.CharField(max_length=160 , blank=True, null=True)
    Meta_keyworads = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('-created','-modified')
    
    def __str__(self):
        return f'{self.Blogtiltle} Blog'
    
    def get_absolute_url(self):
        return reverse('BlogPostview', kwargs={'slug':self.slug})
    
    def get_dashboard_url(self):
        return reverse('dashboard',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None:
            rndmstr = random_digita_generator(size=6)
            self.slug = slugify(self.Blogtiltle+'-'+rndmstr)
        return super().save(*args, **kwargs)
        


class BlogAdmin(admin.ModelAdmin):
    list_display = ('Blogtiltle', 'ReadyToShow')
    
admin.site.register(Blog, BlogAdmin)
    
#class blogcontent(models.Model):
  #  #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #user = models.OneToOneField(Blog, on_delete=models.CASCADE)
    #content = models.CharField(max_length=429, blank=True, null=True)

class Comments(models.Model):
    Comment = models.CharField(max_length=160)
    Commentfrom = models.ForeignKey(User,related_name='Commentfrom', on_delete=models.CASCADE)
    Commenton = models.ForeignKey(Blog,related_name='Commenton', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Comment} Comments'
        
class searched(models.Model):
    USER = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE, blank=True, null=True)
    ip = models.CharField(max_length=40, editable=False, null=True)
    SearchQ = models.CharField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.SearchQ} searched'
        
class searchAdmin(admin.ModelAdmin):
    list_display = ('USER', 'SearchQ','created')
    
admin.site.register(searched, searchAdmin)
    

    
