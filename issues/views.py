from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from projects.models import Project
from .models import Issue
from .serializers import IssueSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Issues"], summary="List and create issues")
class IssueListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs['project_id'])

    def get_queryset(self):
        return Issue.objects.filter(project=self.get_project())

    def perform_create(self, serializer):
        serializer.save(
            project=self.get_project(),
            reporter=self.request.user,
        )
