from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('users/' , views.UserListView.as_view() , name='user-list'),
    path('users/<int:pk>' , views.UserDetailView.as_view() , name='user-detail'),
    path('users/<int:pk>/edit' , views.UserUpdateView.as_view() , name='update-user'),
    path('users/<int:pk>/delete' , views.UserDeleteView.as_view() , name='delete-user'),
    path('users/<int:pk>/toggle-role/', views.ToggleUserRoleView.as_view(), name='toggle-role'),
    
    path("auth/signup",views.SignUpView.as_view(), name="signup"),
    
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password-change-form.html',
        success_url='/password-change/done/'  # Redirect after successful change
    ), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-change-done.html'
    ), name='password-change_done'),
    
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/new' , views.ProjectCreateView.as_view() , name='create-project'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/edit' , views.ProjectUpdateView.as_view() , name='update-project'),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='delete-project'),
    
    path('about/' , views.AboutView.as_view() , name='about-us'),
    
]
