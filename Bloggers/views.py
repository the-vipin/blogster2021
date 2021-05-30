# Create your views here.
from blogster.imports.CommanImportsForViews import *

# Create your views here.
class Bloggerlist(LoginRequiredMixin, ListView):
    login_url = 'sign-in'
    model = Blogger
    


class DashboardSettings(LoginRequiredMixin,UserPassesTestMixin,DetailView):
#class BloggerDashboard(DetailView):
    model = Blogger
    template_name = 'new_temp/dashboard/dashboardSetting.html'
    login_url = 'sign-in'

    def get_context_data(self, **kwargs):
        context = super(DashboardSettings, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger))
        context['TITLE'] = 'dashboard ' + Blogger.BloggerName
        return context
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user == Blogger.Founder:
            return True
        return False

class BloggerDashboard(LoginRequiredMixin,UserPassesTestMixin,DetailView):
#class BloggerDashboard(DetailView):
    model = Blogger
    template_name = 'new_temp/dashboard/dashboardHome.html'
    login_url = 'sign-in'

    def get_context_data(self, **kwargs):
        context = super(BloggerDashboard, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        context['Members'] = User.objects.all()
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger))
        context['TITLE'] = 'dashboard ' + Blogger.BloggerName
        return context
    
    def test_func(self):
        Blogger = self.get_object()
        if self.request.user == Blogger.Founder:
            return True
        return False

class BloggerView(DetailView):
    model = Blogger
    template_name = 'new_temp/pages/bloggerchhannel.html'

    def get_context_data(self, **kwargs):
        context = super(BloggerView, self).get_context_data(**kwargs)
        Blogger = self.get_object()
        #context['Members'] = User.objects.all()
      #  context['meta'] = [x for x in metadatajson if(x['VIEW'] == 'viewblogger')],
        context['Blogslist'] = Blog.objects.filter(Q(BloggerAc=Blogger),Q(ReadyToShow=True)).order_by('-created')
        context['TITLE'] = Blogger.BloggerName+'  - Blogster.co.in'
        context['description'] = Blogger.About 
        return context
    




