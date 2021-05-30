
from users import views

from blogster.imports.CommanImportsForUrl import *
from blogster.ViewsListMap import * 


urlpatterns = [
    path('', profile , name='profile'),
    url(r'sign-up/', views.signup, name="account_signup"),
    url(r'sign-in/', views.Emaillogin, name='sign-in'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('update/',updateprofile, name='update-profile'),
    path('Liked/', LikedBlogpost.as_view(), name='likedblogs'),
    path('Saved/', SavedBlogpost.as_view(), name='readinglist'),
    path('mychannels/', myblocchannellist.as_view(), name='mychannelslist-user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
