
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from infodata.models import FAQs
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView, RedirectView




class Faqpage(ListView):
    model = FAQs
    template_name = 'staffcontrol/faq/faqpage.html'

class create_FAq_for_Faqpage(CreateView):
    model = FAQs
    template_name = 'staffcontrol/faq/create_faq.html'
    login_url = 'sign-in'
    fields = ['Que','Short_Ans','Quetype']
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        return super().form_valid(form)

class Edit_Faq(UpdateView):
    model = FAQs
    template_name = 'staffcontrol/faq/create_faq.html'
    login_url = 'sign-in'
    fields = ['Que','Short_Ans','Quetype']
    success_url = '/'
    
    def form_valid(self, form, *args, **kwargs):
        return super().form_valid(form)

class Delete_Faq(DeleteView):
    model = FAQs
    template_name =  'staffcontrol/delete.html'
    login_url = 'sign-in'
    success_url = '/'





