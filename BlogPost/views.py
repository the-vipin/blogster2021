# Create your views here.
from blogster.imports.CommanImportsForViews import *

# Create your views here.
class Bloglist(ListView):
    model = Blog

class BlogAnalyseView(DetailView):
    model = Blog
    template_name = 'new_temp/form/BlogAnalyis.html'

class Blogview(HitCountDetailView, FormMixin):
    model = Blog
    template_name =  'new_temp/pages/blogpage.html'
    count_hit = True
    form_class = Commentform
    
    def get_success_url(self):
        return reverse('BlogPostview', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(Blogview, self).get_context_data(**kwargs)
        context['form'] = Commentform(initial={
            'Commenton': self.object,
            'Commentfrom': self.request.user
        })
        context['blogpost_comments'] = Blog.objects.annotate(total_comments = Count('Commenton'))
        context['comment_list'] = Comments.objects.filter(Q(Commenton_id=self.object.id))
        CG = self.get_object()
        context['TITLE'] = str(CG.Blogtiltle) + str(CG.BloggerAc.BloggerName)
        context['DICS'] = str(CG.Discription)
        context['KEYWOARDS'] = str(CG.Meta_keyworads) + str(CG.BloggerAc.BloggerName) 
        #context['comments'] = self.object.comment_set.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(Blogview, self).form_valid(form)
    




        




        
