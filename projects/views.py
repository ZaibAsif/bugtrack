from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Project
from .serializers import ProjectSerializer


@extend_schema(tags=["Projects"], summary="List and create projects")
class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)


@extend_schema(tags=["Projects"], summary="Retrieve, update or delete a project")
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)


