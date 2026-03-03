from rest_framework import serializers
from projects.serializers import ProjectSerializer
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'project', 'title', 'description', 'status', 'priority', 'severity', 'created_at', 'updated_at']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)