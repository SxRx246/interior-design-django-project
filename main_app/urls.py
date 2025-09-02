from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/new' , views.ProjectCreateView.as_view() , name='create-project'),
    
    path('designers/' , views.DesignerListView.as_view() , name='designer-list'),
    
    path("auth/signup",views.SignUpView.as_view(), name="signup"),
]
