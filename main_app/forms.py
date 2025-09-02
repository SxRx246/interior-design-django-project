from django import forms
from .models import Project 
# , User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User=get_user_model()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'description', 'pictures', 'designer']

# class LoginFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'role']
        

class SignUpForm(UserCreationForm):
    
    # username = forms.CharField(max_length=30, required=True)
    # password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    
    # class Meta:
    #     model=User
    #     fields = ['username','first_name', 'last_name', 'email']