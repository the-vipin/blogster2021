from blogster.imports.CommanImportsForViews import *


def profile(request):
    if request.user.is_authenticated:
        blogpages = Blogger.objects.filter(Q(Founder=request.user))
        context = {
            'blogpages' : blogpages,
        }
        return render(request, 'new_temp/pages/profilePage.html', context)
    else:
        return render(request, 'new_temp/pages/unregisterProfilePage.html')
        
@login_required
def updateprofile(request):
    if request.method == 'POST':
        form = UserUpdateform(request.POST, request.FILES, instance=request.user)
        if form.is_valid() :
            form.save()
            return redirect('profile')
    form = UserUpdateform(instance=request.user)
    context = {
        'form' : form,
        'TITLE': 'Edit Profile',
    }
    return render(request, 'new_temp/form/updateprofile.html', context)
        