# Create your views here.
from blogster.imports.CommanImportsForViews import *


def home(request):
    #Meta = sql_database_conn.execute(Metadata_views.select().where(Metadata_views.c.View=='jiv'))
    context = {
         #   'meta' : Meta.fetchall(),
            'meta': [x for x in metadatajson if(x['VIEW'] == 'home')],
            'Blogslist': Blog.objects.filter(Q(ReadyToShow=True)).order_by('-created')
    }
    return render(request, 'new_temp/pages/home.html', context)

    

def subscribed(request):
    context = {
        'meta': [x for x in metadatajson if(x['VIEW'] == 'subscribedbloggers')],
        'Blogslist': Blog.objects.filter(Q(ReadyToShow=True),Q(BloggerAc_subscribers=request.user)).order_by('-created')
    }
    return render(request, 'new_temp/pages/home.html', context)

def Help(request):
    return render(request, 'About/help.html')

def about(request):
    return render(request, 'outsrc/landingpage/consult-opl/index.html')

def term_cond(request):
    return render(request, 'About/T&c.html')

def Search(request):
    if request.method == 'POST':
        form = searchedquery(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.ip = get_ip(request)
            user = request.user
            if user.is_authenticated:
                search.USER = request.user 
            search.save()
        query = request.POST.get('SearchQ')
        #searchlist = searched.object.all()
        #searchlist.SearchQ = query
        context = {
            'meta': [x for x in metadatajson if(x['VIEW'] == 'search')],
            'Blogslist': Blog.objects.filter(Q(ReadyToShow=True) ,( Q(Blogtiltle__icontains=query) |Q(Discription__icontains=query) )).order_by('-created'),
            'searched':query,
            'form' : searchedquery()
        }
        return render(request, 'new_temp/pages/searchresult.html', context)
    context= {
        'meta': [x for x in metadatajson if(x['VIEW'] == 'search')],
        'form' : searchedquery()
    }
    return render(request, 'new_temp/pages/searchresult.html', context)