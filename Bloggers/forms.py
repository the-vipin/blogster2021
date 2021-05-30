from django import forms
from django.contrib.auth.models import User
from .models import Blogger

#class manage_blogger_seo(forms.ModelForm):
    #Meta_discription = forms.Textarea(widget=forms.TextInput(attrs={'placeholder':'write discription (this will help your audience to find you)'}))
    #Meta_discription = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'write discription (this will help your audience to find you)'}))
 #   Meta_keyworads = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'write right keywords which related to your blog and seperate them with , comma. ex. blog, bloggers, best blogging platform, free blogs '}))
  #  class Meta:
   #     model = Blogger
    #    fields = ['Meta_discription','Meta_keyworads']
     #   widgets = {
      #      'Meta_discription': forms.Textarea(
       #         attrs={
        #            'placeholder': 'Enter description here',
                 #   'cols': 80,
         #           'rows': 5
          #      }),
        #}
