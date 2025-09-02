from django import forms
from .models import Project , User

class ProjectFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'description', 'pictures', 'designer']

# class LoginFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'role']
        
    