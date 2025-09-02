from django import forms
from .models import Project , User

class ProjectFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'description', 'pictures', 'designer']
        