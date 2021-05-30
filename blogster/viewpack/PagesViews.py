# Create your views here.
from blogster.imports.CommanImportsForViews import *


class LikedBlogpost(LoginRequiredMixin, ListView):
    model = Blog 
    template_name = 'new_temp/pages/LikedBlogsListPage.html'
    context_object_name = 'Blogslist'
    login_url = 'sign-in'

    def get_queryset(self):
        result = super(LikedBlogpost, self).get_queryset()
        query = self.request.user
        if query:    
            result = Blog.objects.filter(
                Q(likes=query) )
        else:
            result = None
        return result
        

class SavedBlogpost(LoginRequiredMixin, ListView):
    model = Blog 
    template_name = 'new_temp/pages/LikedBlogsListPage.html'
    context_object_name = 'Blogslist'
    login_url = 'sign-in'

    def get_queryset(self):
        result = super(SavedBlogpost, self).get_queryset()
        query = self.request.user
        if query:    
            result = Blog.objects.filter(
                Q(save_readlater=query) )
        else:
            result = None
        return result
        
        
class myblocchannellist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    template_name = 'new_temp/pages/myblogchannel.html'
    
    def get_context_data(self, **kwargs):
        context = super(myblocchannellist, self).get_context_data(**kwargs)
        blogpages = Blogger.objects.filter(Q(Founder=self.request.user))
        context['blogpages'] = blogpages
        return context

class subscribedBloggerlist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    template_name = 'new_temp/pages/SubscribedBlogChannel.html'

    def get_context_data(self, **kwargs):
        context = super(subscribedBloggerlist, self).get_context_data(**kwargs)
        context['bloggers'] = Blogger.objects.all()
        return context