
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from Bloggers.views import (
    BloggerCreate,
    BloggerView,
    BloggersubscribersToggle,
    subscribedBloggerlist,
)
from BlogPost.views import (
    BlogCreate,
)
from BlogPost import new_view as blogpost_view

from django.contrib.sitemaps.views import sitemap

from .sitemaps import BlogSitemap, BloggerSitemap, HelpCenterSitemap
from django.views.generic import TemplateView

from infodata.urlpack import helpurls, abouturls
from staffcontrol import urls as staffurls


sitemaps = {
    'blogs': BlogSitemap,
    'bloggers': BloggerSitemap,
    'helpcenters': HelpCenterSitemap,
}     
urlpatterns = [
    path('CEO/', admin.site.urls),
    path('', views.home, name='home'),
    path('help/', include(helpurls)),
    path('about/', include(abouturls)),
    path('1blogster2stafff3page4forediton/', include(staffurls)),
   # path('subscribedblogpost/', views.subscribed , name="subscribedblogpost"),
    path('search/', views.Search , name='search'),
    path('privacy&policy/', views.term_cond , name='t&c'),
    path('accounts/', include('django.contrib.auth.urls')),
   # path('account/', include('allauth.urls')),
    path('me/', include('users.urls')),
    path('DashBoard/', include('Bloggers.urls')),
    path('createblogger/', BloggerCreate.as_view(), name="createblogger"),
    #path('Blogger/<slug:slug>', BloggerView.as_view(), name='viewblogger'),
    #path('Blogger/<slug:slug>/subscribe', BloggersubscribersToggle.as_view(), name='bloggersubscribetoggle'),
    path('<slug:slug>', BloggerView.as_view(), name='viewblogger'),
    path('<slug:slug>/subscribe', BloggersubscribersToggle.as_view(), name='bloggersubscribetoggle'),
   # path('createBlog/<slug:slug>', BlogCreate.as_view(), name="createBlog"),
   # path('edit/<slug:slug>', Editblogcontent.as_view(), name='editblogcontent'),
    path('Create/<slug:slug>', blogpost_view.blogCreate_view.as_view(), name="createBlog"),
    path('Editor/<slug:slug>', blogpost_view.blogEdit_view.as_view(), name='editblogcontent'),
    path('Blog/', include('BlogPost.urls')),
    path('Subscribed/', subscribedBloggerlist.as_view(), name='subscribedbloggers'),
    ####################################################################################
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    path('.well-known/acme-challenge/thSiirVRN0HKHdS_omGCFoMJqlRNoZuARPxvvikIXZc', TemplateView.as_view(template_name=".well-known/acme-challenge/thSiirVRN0HKHdS_omGCFoMJqlRNoZuARPxvvikIXZc", content_type="text/plain"), name="r_file"),
    path('.well-known/acme-challenge/Pn-NCujhXcUvDtNS87iLCEd69pZ_6JZc9i8FF3czI6I', TemplateView.as_view(template_name=".well-known/acme-challenge/Pn-NCujhXcUvDtNS87iLCEd69pZ_6JZc9i8FF3czI6I", content_type="text/plain"), name="r_file")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

