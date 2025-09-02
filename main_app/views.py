from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from models import User , Project
from .forms import ProjectFrom

# Create your views here.

class UserIsAdminMixIn(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return  u.role == u.Role.ADMIN
    
class UserIsDesignerMixIn(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return  u.role == u.Role.DESIGNER

# Change user to admin
class ToggleAdminRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):

    def post(self, request, *args, **kwargs):
        target = get_object_or_404(User, pk=kwargs["pk"])

        target.role = (
            User.Role.ADMIN if target.role != User.Role.ADMIN else User.Role.CUSTOMER
        )
        target.save(update_fields=["role"])
        return redirect("user-list")
    
# project views

class ProjectCreateView(LoginRequiredMixin, UserIsDesignerMixIn, CreateView):
    model = Project
    form_class = ProjectFrom
    template_name = 'projects/project-form.html'
    
    

