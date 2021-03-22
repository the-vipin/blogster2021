from django import forms
from django.contrib.auth.models import User
from .models import Comments ,Blog, searched

class Commentform(forms.ModelForm):
    Comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write your thoughts here'}))
    class Meta:
        model = Comments 
        exclude = ('admitted',)
        widgets = {
            'Commenton': forms.HiddenInput(),
            'Commentfrom': forms.HiddenInput()
        }
        
class blogcreationform(forms.ModelForm):
    Blogtiltle = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
    class Meta:
        model = Blog
        fields = ['Blogtiltle','UpBlog']
        
class manage_blog_seo(forms.ModelForm):
    Meta_keyworads = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'write right keywords which related to your blog and seperate them with , comma. ex. blog, bloggers, best blogging platform, free blogs '}))
    class Meta:
        model = Blog
        fields = ['Meta_discription','Meta_keyworads']
        widgets = {
            'Meta_discription': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description here',
                 #   'cols': 80,
                    'rows': 5
                }),
        }
      
class searchedquery(forms.ModelForm):
    class Meta:
        model = searched
        fields = ['SearchQ']
    

###################################################################
#
class blogEditform(forms.ModelForm):
    Blogtiltle = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Title'}))
    UpBlog = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'explore your mind here'}))
    class Meta:
        model = Blog
        fields = ['Blogtiltle','UpBlog',]    
  
