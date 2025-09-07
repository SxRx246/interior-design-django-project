from django import forms
from .models import Project 
from datetime import date
# , User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User=get_user_model()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'description', 'pictures', 'designer']
         
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Set the max attribute for the date field widget
    #     self.fields['date'].widget.attrs['max'] = date.today()

    # def clean_date(self):
    #     """
    #     Server-side validation to ensure the date is not in the future.
    #     """
    #     selected_date = self.cleaned_data['date']
    #     if selected_date > date.today():
    #         raise forms.ValidationError("The project date cannot be in the future.")
    #     return selected_date
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