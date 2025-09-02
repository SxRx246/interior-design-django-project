from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectListView.as_View(), name='project-list'),
    path('projects/new' , views.ProjectCreateView.as_view() , name='create-project'),
]
