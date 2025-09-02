from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from models import User

# Create your views here.

class UserIsAdminMixIn(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return  u.role == u.Role.ADMIN
    
class UserIsDesignerMixIn(UserPassesTestMixin):
    def test_func(self):
        u = self.request.user
        return  u.role == u.Role.DESIGNER

class ProductCreateView(LoginRequiredMixin, UserIsDesignerMixIn, CreateView):
    pass


# Change user to admin
class ToggleAdminRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):

    def post(self, request, *args, **kwargs):
        target = get_object_or_404(User, pk=kwargs["pk"])

        target.role = (
            User.Role.ADMIN if target.role != User.Role.ADMIN else User.Role.CUSTOMER
        )
        target.save(update_fields=["role"])
        return redirect("user-list")