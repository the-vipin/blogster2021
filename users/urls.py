from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from users import views
from BlogPost.views import (
    LikedBlogpost,SavedBlogpost,
)
from Bloggers.views import (
    myblocchannellist,
)

urlpatterns = [
    path('', views.profile, name='profile'),
    url(r'sign-up/', views.signup, name="account_signup"),
    url(r'sign-in/', views.Emaillogin, name='sign-in'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_account, name='activate'),
    path('update/', views.updateprofile, name='update-profile'),
    path('Liked/', LikedBlogpost.as_view(), name='likedblogs'),
    path('Saved/', SavedBlogpost.as_view(), name='readinglist'),
    path('mychannels/', myblocchannellist.as_view(), name='mychannelslist-user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
