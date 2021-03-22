from django.contrib.sitemaps import Sitemap
from BlogPost.models import Blog
from Bloggers.models import Blogger
from infodata.models import HelpCenter
from django.urls import reverse

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Blog.objects.all()
        
    def location(self, item):
        return reverse('BlogPostview',kwargs={'slug':item.slug})
        
class BloggerSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Blogger.objects.all()
        
    def location(self, item):
        return reverse('viewblogger',kwargs={'slug':item.slug})

class HelpCenterSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return HelpCenter.objects.all()
        
    def location(self, item):
        return reverse('about-hc-artical-read',kwargs={'pk':item.id})



        

