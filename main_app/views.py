from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import User , Project
from .forms import ProjectForm, SignUpForm, UserForm
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

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
    
# Change user to designer
class ToggleDesignerRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):

    def post(self, request, *args, **kwargs):
        target = get_object_or_404(User, pk=kwargs["pk"])

        target.role = (
            User.Role.DESIGNER if target.role != User.Role.DESIGNER else User.Role.CUSTOMER
        )
        target.save(update_fields=["role"])
        return redirect("user-list")
    
    
# designer views
# class DesignerListView(ListView):
#     model = User
#     template_name = 'designers/designer-list.html'
#     context_object_name = 'designers'
    
# class DesignerDetailView(DetailView):
#     model = User
#     template_name = 'designers/designer-detail.html'
#     context_object_name = 'designer'

# user views
class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'users/user-list.html'
    context_object_name = 'users'
    
class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'users/user-detail.html'
    context_object_name = 'user'
    
class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'users/user-form.html'
    form_class = UserForm
    success_url = reverse_lazy('user-detail')
    
class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
    

# class DesignerCreateview(CreateView):
#     model = User
#     template_name = 
 
# project views

class ProjectListView(LoginRequiredMixin, UserIsDesignerMixIn, ListView):
    model=Project
    template_name = 'projects/project-list.html'
    context_object_name = 'projects'

class ProjectCreateView(LoginRequiredMixin, UserIsDesignerMixIn, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project-form.html'
    
    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.object.pk})

    
    

