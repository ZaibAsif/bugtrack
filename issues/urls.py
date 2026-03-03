from django.urls import path
from .views import IssueListCreateView

app_name = 'issues'

urlpatterns = [
    path('', IssueListCreateView.as_view(), name='issue-list-create'),
]
