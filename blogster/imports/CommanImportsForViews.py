import math, random , smtplib
import time
import json
import string
import urllib.request
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.template.loader import get_template, render_to_string
from django.template import RequestContext

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import HttpResponseRedirect
from django.http import HttpResponse, request

from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView, FormView
from django.views.generic.edit import ModelFormMixin, UpdateView, FormMixin
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, EmailMessage

from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.urls import reverse
from django.urls.base import reverse

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from hitcount.views import HitCountDetailView
from django.db.models import Count, Q
from itertools import chain
from string import Template
from django.template import RequestContext

#from Blogger
from Bloggers.models import Blogger

#from BlogPost
from BlogPost.models import Blog, searched, Comments
from BlogPost.forms import Commentform, blogcreationform, manage_blog_seo, searchedquery, blogEditform

#from Blogster
from blogster.util import get_ip
from blogster.settings import metadatajson, metadataformjson

#from users
from users.forms import UserRegisterform, UserUpdateform, UserEmailLoginform
from users.token_generator import account_activation_token


