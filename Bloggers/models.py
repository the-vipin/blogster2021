from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.db.models.signals import pre_save
import os
from django.urls import reverse
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.utils.text import slugify

# Create your models here.

def compraseImg(path):
    img = Image.open(path) # Open image using self
    img.thumbnail((300, 300))
    return img.save(path)

class Blogger(models.Model):
    Account = [
        ('Affiliate-Blogs','Affiliate Blogs'),
        ('Books-Blogs','Books Blogs'),
        ('Business-Blogs','Business Blogs'),
        ('Car-Blogs','Car Blogs'),
        ('Corporate-Blog', 'Corporate Blog'),
        ('Case-Study-Blogs', 'Case Study Blogs'),
        ('Contests','Contests'),
        ('Controversial-Subjects','Controversial Subjects'),
        ('DIY-Blogs','DIY Blogs'),
        ('Debates', 'Debates'),
        ('Entertainment-Blogs','Entertainment Blogs'),
        ('Event-Summaries','Event Summaries'),
        ('Fashion-blogs', 'Fashion blogs'),
        ('Finance-Blogs','Finance Blogs'),
        ('Fitness-Blogs', 'Fitness Blogs'),
        ('Food-Blogs','Food Blogs'),
        ('Freelance-bloggers','Freelance bloggers'),
        ('Gaming-blogs','Gaming Blogs'),
        ('How-to-Blogs', 'How-to Blogs'),
        ('Inspirational-Blogs','Inspirational Blogs'),
        ('Interviews','Interviews'),
        ('Lifestyle-Blogs','Lifestyle Blogs'),
        ('Listicles', 'Listicles'),
        ('Movie-Blogs','Movie Blogs'),
        ('Music-Blogs','Music Blogs'),
        ('News-blogs', 'News Blogs'),
        ('Parenting-Blogs', 'Parenting Blogs'),
        ('Personal-Blogs','Personal Blogs'),
        ('Personal-Services-Blog','Personal Services Blog'),
        ('Pet-Blogs','Pet Blogs'),
        ('Podcast','Podcast'),
        ('Political-Blogs','Political Blogs'),
        ('Professional-Blogs','Professional Blogs'),
        ('Reviews','Reviews'),
        ('Surveys-and-Polls','Surveys and Polls'),
        ('Sports-Blogs','Sports Blogs'),
        ('Tutorials','Tutorials'),
        ('Travel-Blogs','Travel Blogs'),
        ('The-Counter-Culture-Blogs','The Counter-Culture Blogs'),
        ('Writing-Blogs','Writing Blogs'),
        ('Poetry','Poetry'),
    ]
    image = models.ImageField(default='team.png', upload_to='Blogger_profile/')
    BloggerName = models.CharField(max_length=60, unique=True)
    Founder = models.ForeignKey(User,related_name='Founders', on_delete=models.PROTECT)
    About = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers',blank=True)
    Accounttype = models.CharField(max_length=100, choices = Account, blank=True, default='Personal-Blogs')

    
    personal_websitelink = models.URLField(max_length=300, blank=True)
    #social media link fields end

    def __str__(self):
        return self.BloggerName
    
    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'slug':self.slug})
    
    def get_bloggerview_url(self):
        return reverse('viewblogger', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.BloggerName)
        super(Blogger, self).save(*args, **kwargs)
        compraseImg(self.image.path)


    
    

