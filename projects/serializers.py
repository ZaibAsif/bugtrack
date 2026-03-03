from rest_framework import serializers
from .models import Project, ProjectRole


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'status']
        read_only_fields = ['id']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        request = self.context.get('request')
        if request and request.user:
            ProjectRole.objects.create(project=project, user=request.user, role='admin')
        return project