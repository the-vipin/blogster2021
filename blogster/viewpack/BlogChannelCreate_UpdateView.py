# Create your views here.
from blogster.imports.CommanImportsForViews import *

class BloggerCreate(LoginRequiredMixin, CreateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['image','BloggerName','Accounttype']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        instances.Founder = self.request.user
        instances = form.save(commit=True)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(BloggerCreate, self).get_context_data(**kwargs)
        context['TITLE'] = 'Blogger creation form'
        context['formtype'] = 'Bloggercreation'
        context['submit_button_name'] = 'Create'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'sign up in blogster and join the community of innovative and revulationary minds. explore your mind. expand your reading. expand your knowledge'
        return context

class UpdateBlogger(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blogger
    template_name =  'new_temp/form/bloggerform.html'
    login_url = 'sign-in'
    fields = ['image','BloggerName','About','Accounttype']
    success_url = '/'

    def form_valid(self, form):
        instances = form.save(commit=False)
        instances.Founder = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user == Blogger.Founder:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(UpdateBlogger, self).get_context_data(**kwargs)
        context['TITLE'] = 'Update blogger details'
        context['formtype'] = 'Bloggerupdate'
        context['submit_button_name'] = 'Save details'
        context['keywoards'] = 'blog creation, blog creation free, blog creation website, blog creation for free, blog creation in wordpress, blog creation in google, blog creation in blogster, blogster, blogs, blogstar, blogbustor'
        context['description'] = 'sign up in blogster and join the community of innovative and revulationary minds. explore your mind. expand your reading. expand your knowledge'
        return context
        
