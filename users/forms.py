from __future__ import unicode_literals
from .utils import _
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings

UserModel = get_user_model
def UsernameField():
    return getattr(UserModel(), 'USERNAME_FIELD', 'username')

class UserRegisterform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1', 'password2']
        
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email'] , is_active=True).exists():
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        else:
            if User.objects.filter(email__iexact=self.cleaned_data['email'] , is_active=False).exists():
                    User.objects.filter(email__iexact=self.cleaned_data['email'], is_active=False).delete()
                    return self.cleaned_data['email']
        return self.cleaned_data['email']
    
#class UserRegisterform(UserCreationForm):
 #   email = forms.EmailField()
  #  class Meta:
   #     model = User
    #    fields = ['email','username','password1', 'password2']
#    def clean_username(self):
 #       username = self.cleaned_data.get('username', '').lower()
  #      if User.objects.filter(username=username).exists():
   #         raise forms.ValidationError(_('A user with that username already exists.'))
    #    return username
#    def clean_email(self):
 #       """
  #      Validate that the supplied email address is unique for the
   #     site.
    #    """
     #   if User.objects.filter(email__iexact=self.cleaned_data['email'] , is_active=True).exists():
      #      raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
       # else:
        #    if User.objects.filter(email__iexact=self.cleaned_data['email'] , is_active=False).exists():
         #           User.objects.filter(email__iexact=self.cleaned_data['email'], is_active=False).delete()
          #          return self.cleaned_data['email']
#        return self.cleaned_data['email']

class UserUpdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('A user with that username already exists.'))
        return username
        
        
class UserEmailLoginform(forms.ModelForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta:
        model = User
        fields = ['email','password']
    
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email'] , is_active=True).exists():
            return self.cleaned_data['email']
        else:
            raise forms.ValidationError(_("We can not find your email on blogster"))
            
            
        