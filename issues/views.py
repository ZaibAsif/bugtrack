from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from projects.models import Project
from .models import Issue
from .serializers import IssueSerializer
from drf_spectacular.utils import extend_schema
from .models import Comment
from .serializers import CommentSerializer
from .models import CommentReply
from .serializers import CommentReplySerializer

@extend_schema(tags=["Issues"], summary="List and create issues")
class IssueListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs['project_id'])

    def get_queryset(self) -> QuerySet[Issue]:
        return Issue.objects.filter(project=self.get_project())

    def perform_create(self, serializer):
        serializer.save(
            project=self.get_project(),
            reporter=self.request.user,
        )
@extend_schema(tags=["Comments"], summary="List and create comments")
class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_issue(self):
        return get_object_or_404(Issue, pk=self.kwargs['issue_id'])

    def get_queryset(self) -> QuerySet[Comment]:
        return Comment.objects.filter(issue=self.get_issue())

    def perform_create(self, serializer):
        serializer.save(
            issue=self.get_issue(),
            author=self.request.user,
        )
@extend_schema(tags=["Comments"], summary="Update a comment")
class CommentUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@extend_schema(tags=["Comments"], summary="List and create replies to a comment")
class ReplyCommentView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer

    def get_comment(self):
        return get_object_or_404(Comment, pk=self.kwargs['comment_id'])

    def get_queryset(self) -> QuerySet[CommentReply]:
        return CommentReply.objects.filter(comment=self.get_comment())

    def perform_create(self, serializer):
        serializer.save(
            comment=self.get_comment(),
            author=self.request.user,
        )