from django.urls import path, include
from .views import ProjectListCreateView, ProjectDetailView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:project_id>/issues/', include('issues.urls')),
]
