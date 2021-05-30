from blogster.imports.CommanImportsForUrl import *

from staffcontrol import views
from staffcontrol.viewpack import faq_view as faqv

urlpatterns = [
    path('', views.homepage , name='staffcontrol-home'),
    
    path('helpcenterpage/', views.helpcenterpage.as_view() , name='staffcontrol-helpcenterpage'),
    path('helpcenterpage/createarticle/', views.create_article_for_helpcenterpage.as_view() , name='staffcontrol-create_article_for_helpcenterpage'),
    path('helpcenterpage/artical/<int:pk>/edit', views.Edit_artical.as_view() , name='staffcontrol-helpcenterpage-artical-edit'),
    path('helpcenterpage/artical/<int:pk>/delete', views.Delete_artical.as_view() , name='staffcontrol-helpcenterpage-artical-del'),

    path('faqpage/', faqv.Faqpage.as_view()  , name='staffcontrol-faqpage'),
    path('faqpage/createfaq/', faqv.create_FAq_for_Faqpage.as_view() , name='staffcontrol-create_article_for_faqpage'),
    path('faqpage/faq/<int:pk>/edit', faqv.Edit_Faq.as_view() , name='staffcontrol-faqpage-artical-edit'),
    path('faqpage/faq/<int:pk>/delete', faqv.Delete_Faq.as_view() , name='staffcontrol-faqpage-artical-del'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
