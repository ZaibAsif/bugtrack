from django.urls import path
from .views import IssueListCreateView
from .views import CommentListCreateView, ReplyCommentView


app_name = 'issues'

urlpatterns = [
    path('', IssueListCreateView.as_view(), name='issue-list-create'),
    path('<int:issue_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:issue_id>/comments/<int:comment_id>/replies/', ReplyCommentView.as_view(), name='reply-comment-list-create'),
]
