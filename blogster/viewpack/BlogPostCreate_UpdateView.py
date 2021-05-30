# Create your views here.
from blogster.imports.CommanImportsForViews import *

class blogCreate_view(LoginRequiredMixin, CreateView, FormMixin):
    model = Blog
    template_name =  'new_temp/form/blogEditor.html'
    login_url = 'sign-in'
    form_class = blogEditform
  #  success_url = '/'
    def get_success_url(self):
        return reverse('blog-analyse', kwargs={'slug': self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        instances = form.save(commit=False)
        instances.Uploader = self.request.user
        slug = self.kwargs.get("slug")
        instances.BloggerAc = get_object_or_404(Blogger, slug=slug)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(blogCreate_view, self).get_context_data(**kwargs)
        context['TITLE'] = 'create blogpost'
        return context
        
class blogEdit_view(LoginRequiredMixin,UserPassesTestMixin, UpdateView, FormMixin):
    model = Blog
    template_name =  'new_temp/form/blogEditor.html'
    login_url = 'sign-in'
    form_class = blogEditform
  #  success_url = '/'
    def get_success_url(self):
        return reverse('editblogcontent', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(blogEdit_view, self).get_context_data(**kwargs)
        context['TITLE'] = 'Edit blogpost'
        return context
        

class Manage_Blog_Seo(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name =  'new_temp/form/seoform.html'
    login_url = 'sign-in'
    form_class = manage_blog_seo
    
    def get_success_url(self):
        return reverse('blog-analyse', kwargs={'slug': self.object.slug})
    
    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(Manage_Blog_Seo, self).get_context_data(**kwargs)
        context['TITLE'] = 'Manage Blog Seo'
        context['formtype'] = 'updateblogdetails'
        context['submit_button_name'] = 'Save SEO'
        return context        
    
class UpdateBlog(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name =  'new_temp/form/seoform.html'
    login_url = 'sign-in'
    fields = ['Blogtiltle','Discription','image','Conclusion']
    
    def get_success_url(self):
        return reverse('blog-analyse', kwargs={'slug': self.object.slug})
    
    def form_valid(self, form):
        instances = form.save(commit=False)
        return super().form_valid(form)
    
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.Uploader:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(UpdateBlog, self).get_context_data(**kwargs)
        context['TITLE'] = 'edit blog details'
        context['formtype'] = 'updateblogdetails'
        context['submit_button_name'] = 'Save'
        return context