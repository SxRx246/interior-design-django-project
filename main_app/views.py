from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import User , Project
from .forms import ProjectForm, SignUpForm, UserForm
from django.urls import reverse_lazy, reverse
import os
from django.utils import timezone
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

# class GettingLoggedinUser(DetailView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["logged_in_user"] = self.request.user
#         print(self.request.user)
#         print(self.request.user.role)
        
#         return context
    


# Change user to admin
# class ToggleAdminRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):

#     def post(self, request, *args, **kwargs):
#         target = get_object_or_404(User, pk=kwargs["pk"])

#         target.role = (
#             User.Role.ADMIN if target.role != User.Role.ADMIN else User.Role.CUSTOMER
#         )
#         target.save(update_fields=["role"])
#         return redirect("user-list")
    
# Change user to designer
# class ToggleDesignerRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):

#     def post(self, request, *args, **kwargs):
#         target = get_object_or_404(User, pk=kwargs["pk"])

#         target.role = (
#             User.Role.DESIGNER if target.role != User.Role.DESIGNER else User.Role.CUSTOMER
#         )
#         target.save(update_fields=["role"])
#         return redirect("user-list")

class ToggleUserRoleView(LoginRequiredMixin, UserIsAdminMixIn, View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])

        if user.role == User.Role.CUSTOMER:
            user.role = User.Role.ADMIN
        elif user.role == User.Role.ADMIN:
            user.role = User.Role.DESIGNER
        else:
            user.role = User.Role.CUSTOMER

        user.save(update_fields=["role"])
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_admin'] = User.objects.filter(role=User.Role.ADMIN).count()
        context['count_designer'] = User.objects.filter(role=User.Role.DESIGNER).count()
        context['count_customer'] = User.objects.filter(role=User.Role.CUSTOMER).count()
        
        context["logged_in_user"] = self.request.user
        print(self.request.user)
        print(self.request.user.role)
        
        return context
    
    # queryset = User.objects.filter(role = User.Role.DESIGNER)
    
    # def get_queryset(self):
    #     return User.objects.filter(role = self.kwargs['role'])
    
    
class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'users/user-detail.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_in_user"] = self.request.user
        print(self.request.user)
        print(self.request.user.role)
        
        return context
    
    
class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'users/user-form.html'
    form_class = UserForm
    def get_success_url(self):
        return reverse("user-detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_in_user"] = self.request.user
        print(self.request.user)
        print(self.request.user.role)
        
        return context
    
# def form_valid(self, form):
#     # Handle image replacement/deletion
#     if 'profile_picture' in form.changed_data:
#         old_instance = self.get_object()
#         if old_instance.profile_picture:
#             if os.path.exists(old_instance.profile_picture.path):
#                 os.remove(old_instance.profile_picture.path)

#     return super().form_valid(form)
    
class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
    

# class DesignerCreateview(CreateView):
#     model = User
#     template_name = 
 
# project views

class ProjectListView(LoginRequiredMixin, ListView):
    model=Project
    # template_name = 'projects/project-list.html'
    template_name = 'loaft-master\project.html'
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_in_user"] = self.request.user
        print(self.request.user)
        print(self.request.user.role)
        
        projects = context['projects']
        mid_point = len(projects) // 2
        context['left_projects'] = projects[:mid_point]
        context['right_projects'] = projects[mid_point:]
        
        return context
    
    
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model=Project
    # template_name = 'projects/project-detail.html'
    template_name = 'loaft-master/project-details.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_in_user"] = self.request.user
        print(self.request.user)
        print(self.request.user.role)
        
        return context

# class ProjectCreateView(LoginRequiredMixin, UserIsDesignerMixIn , CreateView):
class ProjectCreateView(LoginRequiredMixin , CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'loaft-master/project-form.html'
    # template_name = 'projects/project-form.html'
    
    def form_valid(self, form):
        # You can add additional processing here if needed
        return super().form_valid(form)

    def form_invalid(self, form):
        # Print form errors to the console for debugging
        print(form.errors)
        return super().form_invalid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     designers = User.objects.filter(role=User.Role.DESIGNER)
    #     context['designers'] = designers
        
    #     context["logged_in_user"] = self.request.user

    #     print(self.request.user)
    #     print(self.request.user.role)

    #     date_value = timezone.now()  
    #     context['date_value'] = date_value.strftime('%Y-%m-%d')

    #     return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        designers = User.objects.filter(role=User.Role.DESIGNER)
        context['designers'] = designers
        
        context["logged_in_user"] = self.request.user

        print(self.request.user)
        print(self.request.user.role)

        # date_value = timezone.now()  
        # context['date_value'] = date_value.strftime('%Y-%m-%d')
        
        form = context.get('form')

        if form:
            # Try to get a valid date from initial or bound data
            date_initial = form.initial.get('date')
            date_bound = form['date'].value()

            # Prefer the initial date, fall back to bound value if needed
            date_value = date_initial if date_initial else date_bound

            # Only format if we have a meaningful value (not None or empty string)
            if date_value:
                # If it's a date object, format it; if string, pass as-is
                context['date_value'] = (
                    date_value.strftime('%Y-%m-%d')
                    if hasattr(date_value, 'strftime')
                    else date_value
                )
            else:
                # Keep the date input empty if no value is set
                context['date_value'] = ''
        else:
            # If no form exists, use today's date as a fallback
            context['date_value'] = timezone.now().strftime('%Y-%m-%d')


        return context
    
    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.object.pk})

    

# class ProjectUpdateView(LoginRequiredMixin, UserIsDesignerMixIn, CreateView):
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'loaft-master/project-form.html'
    # template_name = 'projects/project-form.html'
    def get_success_url(self):
        return reverse("project-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        designers = User.objects.filter(role=User.Role.DESIGNER)
        context['designers'] = designers
        
        context["logged_in_user"] = self.request.user

        print(self.request.user)
        print(self.request.user.role)

        # date_value = timezone.now()  
        # context['date_value'] = date_value.strftime('%Y-%m-%d')
        
        form = context.get('form')

        if form:
            # Try to get a valid date from initial or bound data
            date_initial = form.initial.get('date')
            date_bound = form['date'].value()

            # Prefer the initial date, fall back to bound value if needed
            date_value = date_initial if date_initial else date_bound

            # Only format if we have a meaningful value (not None or empty string)
            if date_value:
                # If it's a date object, format it; if string, pass as-is
                context['date_value'] = (
                    date_value.strftime('%Y-%m-%d')
                    if hasattr(date_value, 'strftime')
                    else date_value
                )
            else:
                # Keep the date input empty if no value is set
                context['date_value'] = ''
        else:
            # If no form exists, use today's date as a fallback
            context['date_value'] = timezone.now().strftime('%Y-%m-%d')


        return context
    
# class ProjectDeleteView(LoginRequiredMixin, UserIsDesignerMixIn, DeleteView):
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')
    
class HomepageView(ListView):
    model = Project
    template_name = 'loaft-master/index.html'
    context_object_name = 'projects'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        projects = context['projects']
        context['left_projects'] = projects[:1]
        context['right_projects'] = projects[1:3]
        return context
    
class AboutView(TemplateView):
    template_name = 'loaft-master/about-us.html'
    

