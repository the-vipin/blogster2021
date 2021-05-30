# Create your views here.
from blogster.imports.CommanImportsForViews import *

class DeleteBlogger(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blogger
    template_name =  'new_temp/form/DeleteConfirmForm.html'
    login_url = 'sign-in'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super(DeleteBlogger, self).get_context_data(**kwargs)
        context['Alert'] = 'Are your Sure you want to delete BlogChannel, or its only a mistake'
        return context

    def test_func(self):
        Blogger = self.get_object()
        if self.request.user == Blogger.Founder:
            return True
        return False
        
class DeleteBlog(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    template_name =  'new_temp/form/DeleteConfirmForm.html'
    login_url = 'sign-in'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super(DeleteBlog, self).get_context_data(**kwargs)
        context['Alert'] = 'Are your Sure you want to delete it Blog, or its only a mistake'
        return context

    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False