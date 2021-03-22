# Create your views here.
import math, random , smtplib
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import UserRegisterform, UserUpdateform, UserEmailLoginform
from django.db.models import Count
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView, FormView
from django.views.generic.edit import ModelFormMixin, UpdateView
from itertools import chain
from django.db.models import Q
from django.urls import reverse
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import get_template, render_to_string
from .token_generator import account_activation_token
from django.utils import timezone
import time
from django.urls.base import reverse
from Bloggers.models import Blogger
from pygments.lexers import d
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, EmailMessage
import string
import random

def random_string_generator(size =4, chars= string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def profile(request):
    blogpages = Blogger.objects.filter(Q(Members=request.user) |Q(Founder=request.user))
        #founderblogpages = Blogger.objects.filter(Q(Founder=request.user))
    context = {
        'blogpages' : blogpages,
        #'founderblogpages' : founderblogpages
    }
    return render(request, 'new_temp/pages/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)            
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            fullname = user.first_name+user.last_name
            user.username = '%s%s' % (fullname, random_string_generator(size=4))
            user.save()
            email_subject = 'Blogster conformation code'
            message = render_to_string('mail/conf_mail.html',{
                'user': user,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
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
        login(request, user)
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
    return render(request, 'new_temp/form/basicform.html', {'form':form,'TITLE': 'Email Login ', 'login_method':'email', 'formtype':'loginform', 'submit_button_name':'LOG IN',})

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
        'description': '',
        'keywoards':'',
        'formtype':'updateprofile',
        'submit_button_name':'Save Details',
    }
    return render(request, 'new_temp/form/basicform.html', context)






