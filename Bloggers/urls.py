from users import views

from blogster.imports.CommanImportsForUrl import *
from blogster.ViewsListMap import * 

urlpatterns = [
    path('<slug:slug>',BloggerDashboard.as_view(), name='dashboard'),
    path('<slug:slug>/setting',DashboardSettings.as_view(), name='dashboard-setting'),
    path('<slug:slug>/Update', UpdateBlogger.as_view(), name='updateblogger'),
  #  path('<slug:slug>/sociallinksupdate', Update_social_media_urls.as_view(), name='updatebloggersociallinks'),
    path('<slug:slug>/Delete', DeleteBlogger.as_view(), name='deleteblogger'),
   # path('<slug:slug>/Manage-SEO', Update_Blogger_SE0.as_view(), name='manage_blogger_seo'),
#    path('<slug:slug>/personal-link', Update_personal_website_link.as_view(), name='updatebloggerpersonallinks'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
