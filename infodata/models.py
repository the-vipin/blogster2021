from django.db import models
from django import forms

class HelpCenter(models.Model):
    gs = [
        ('Getting_Started','Getting Started'),
        ('Login','Login'),
        ('Account_settings','Account settings'),
        ('navigating','navigating'),
        ('Managing_blogs','Managing blogs'),
        ('Terms_&_policies','Terms & policies'),
        ('Others','Others'),
    ]
    subject_name = models.CharField(max_length=1000)
    Group = models.CharField(max_length=100, choices = gs, default='Others')
    articalname = models.CharField(max_length=9999)
    content = models.TextField(blank=True, null=True)

class FAQs(models.Model):
    que_type = [
        ('blogster-terminology','blogster terminology'),
        ('how_to','how to'),
        ('about-Blogster','about Blogster'),
        ('technical_que','technical que'),
        ('Blogging','Blogging'),
    ]
    Que = models.CharField(max_length=9999)
    ShortAns = models.TextField(blank=True, null=True)
    LongAns = models.TextField(blank=True, null=True)
    Quetype = models.CharField(max_length=100, choices = que_type, blank=True, default='about-Blogster')


