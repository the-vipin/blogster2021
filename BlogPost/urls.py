from users import views

from blogster.imports.CommanImportsForUrl import *
from blogster.ViewsListMap import * 

from . import views
urlpatterns = [
    path('<slug:slug>', Blogview.as_view(), name='BlogPostview'),
    #path('<slug:slug>', views.blogview, name='BlogPostview'),
    path('<slug:slug>/Update', UpdateBlog.as_view(), name='updateblog'),
    path('<slug:slug>/Delete', DeleteBlog.as_view(), name='deleteblog'),
    path('<slug:slug>/like', BlogPostlikeToggle.as_view(), name='likeblogpost'),
    path('<slug:slug>/Dislike', BlogPostDislikeToggle.as_view(), name='dislikeblogpost'),
    path('<slug:slug>/Save', BlogPostSaveToggle.as_view(), name='saveblogpost'),
    path('<slug:slug>/comment/post', BlogPostCommentOn.as_view(), name='comment-poston-blogpost'),
    path('<slug:slug>/comment/delete', BlogPostDislikeToggle.as_view(), name='comment-deleteon-blogpost'),
    path('<slug:slug>/Manage-SEO', Manage_Blog_Seo.as_view(), name='manage_blog_seo'),
    path('<slug:slug>/Analyse', BlogAnalyseView.as_view(), name='blog-analyse'),
    
    #path('<slug:slug>/publish', publishblog.as_view(), name='publish-blog'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
