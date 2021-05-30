# Create your views here.
from blogster.imports.CommanImportsForViews import *

def random_string_generator(size =4, chars= string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))


def signup(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)            
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            fullname = user.first_name+user.last_name
            user.username = '%s%s' % (fullname, random_string_generator(size=4))
            user.save()
            email_subject = 'Blogster conformation mail'
            message = render_to_string('mail/conf_mail.html',{
                'user': user,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            
            contextA = {
                'user': user,
                'TITLE': 'registration conformation link sended'
            }
            return render(request,'registration/reg_conf_msg.html', contextA)
    context = {
        'form': UserRegisterform(),
        'TITLE': 'Create new account',
        'description': '',
        'keywoards':'',
        'formtype':'signup',
        'submit_button_name':'CREATE ACCOUNT',
    }
    return render(request, 'new_temp/form/basicform.html', context)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
        return redirect('profile')
    else:
        return HttpResponse('activate link is invalid')
        
def Emaillogin(request):
    if request.method == 'POST':
        form = UserEmailLoginform(request.POST)            
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            username = User.objects.get(email__iexact=email).username
            user = authenticate(username=username, password=password)
            try: 
                request.session['Userauth'] = user.username
                request.session['Userauthpass'] = request.POST['password']
                login(request,user)
                return redirect('profile')
            except User.DoesNotExist:
                return HttpResponse("Your username and password didn't match.")
    form = UserEmailLoginform()
    return render(request, 'account/loginusingEmail.html', {'form':form,'TITLE': 'Email Login ', 'login_method':'email', 'formtype':'loginform', 'submit_button_name':'LOG IN',})








