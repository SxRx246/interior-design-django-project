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
        # fields = ['pictures']
        
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > date.today():
            raise forms.ValidationError("The project date cannot be in the future.")
        return date
        
# class LoginFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'role']
        

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    class Meta:
        model=User
        fields = ['username','first_name', 'last_name', 'email', 'profile_picture']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields =  ['username','first_name', 'last_name', 'email', 'profile_picture']
        fields =  ['profile_picture']