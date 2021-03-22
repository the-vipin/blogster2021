from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from infodata import views as infoview
from infodata.viewpack import aboutview, helpview

urlpatterns = [
    path('feature/', aboutview.textview, name='about-feature'),
    path('landing/', aboutview.textview, name='about-landing'),
    path('benefits/', aboutview.textview, name='about-benefits')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
