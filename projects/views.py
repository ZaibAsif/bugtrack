from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Project
from .serializers import ProjectSerializer


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method == 'POST':
            return (
                getattr(request.user, 'role', None) == 'manager'
            )
        return True


@extend_schema(tags=["Projects"], summary="List and create projects")
class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def get_queryset(self):
    #     return Project.objects.filter(users=self.request.user)


@extend_schema(tags=["Projects"], summary="Retrieve, update or delete a project")
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)


