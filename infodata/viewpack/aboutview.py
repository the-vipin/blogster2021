from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def textview(request):
    return HttpResponse('welcome jiii')
