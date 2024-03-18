from django import forms
from django.contrib.auth.forms import UserCreationForm
from testapp.models import contactus
from django.contrib.auth.models import User
class  contactusform(forms.ModelForm):
    class Meta:
        model=contactus
        fields="__all__"

    
class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
