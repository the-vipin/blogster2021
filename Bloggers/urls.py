from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from users import views
from .views import (
    BloggerDashboard,
    DashboardSettings,
    UpdateBlogger,
    DeleteBlogger,
    Update_social_media_urls,
    Update_Blogger_SE0,
    Update_personal_website_link,
    
)
#from blogster.studio import views

urlpatterns = [
    path('<slug:slug>',BloggerDashboard.as_view(), name='dashboard'),
    path('<slug:slug>/setting',DashboardSettings.as_view(), name='dashboard-setting'),
    path('<slug:slug>/Update', UpdateBlogger.as_view(), name='updateblogger'),
    path('<slug:slug>/sociallinksupdate', Update_social_media_urls.as_view(), name='updatebloggersociallinks'),
    path('<slug:slug>/Delete', DeleteBlogger.as_view(), name='deleteblogger'),
    path('<slug:slug>/Manage-SEO', Update_Blogger_SE0.as_view(), name='manage_blogger_seo'),
    path('<slug:slug>/personal-link', Update_personal_website_link.as_view(), name='updatebloggerpersonallinks'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
