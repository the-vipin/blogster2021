# Create your views here.
from blogster.imports.CommanImportsForViews import *

class BloggersubscribersToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blogger, slug=slug)
        url_ = blog.get_bloggerview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.subscribers.all():
                blog.subscribers.remove(user)
            else:
                blog.subscribers.add(user)
        return url_
        
        
class BlogPostCommentOn(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'
    
    def post_comment(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        if request.method == 'POST':
            form = Commentform(request.POST)
            if form.is_valid():
                #Comment = form.cleaned_data['Comment']
                #blog.comments_set.create(Comment=Comment)
                instances = form.save(commit=False)
                instances.Commentfrom = self.request.user.id
                instances.Commenton = blog.id
                form.save()
                #messages.infos(request,comment)
        return url_

class BlogPostlikeToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.likes.all():
                blog.likes.remove(user)
            else:
                blog.likes.add(user)
                if user in blog.Dislikes.all():
                    blog.Dislikes.remove(user)
        return url_
        
class BlogPostDislikeToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.Dislikes.all():
                blog.Dislikes.remove(user)
            else:
                blog.Dislikes.add(user)
                if user in blog.likes.all():
                    blog.likes.remove(user)
        return url_
        
class BlogPostSaveToggle(LoginRequiredMixin, RedirectView):
    login_url = 'sign-in'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        blog = get_object_or_404(Blog, slug=slug)
        url_ = blog.get_blogview_url()
        user = self.request.user
        if user.is_authenticated:
            if user in blog.save_readlater.all():
                blog.save_readlater.remove(user)
            else:
                blog.save_readlater.add(user)
        return url_