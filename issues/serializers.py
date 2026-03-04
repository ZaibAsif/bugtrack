from rest_framework import serializers
from projects.serializers import ProjectSerializer
from .models import Issue
from .models import Comment
from .models import CommentReply

class IssueSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:  # pyright: ignore
        model = Issue
        fields = ['id', 'project', 'title', 'description', 'status', 'priority', 'severity', 'created_at', 'updated_at']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore
        model = Comment
        fields = ['id', 'issue', 'text', 'author', 'created_at']
        read_only_fields = ['id', 'issue', 'author', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore
        model = CommentReply
        fields = ['id', 'comment', 'text', 'author', 'created_at']
        read_only_fields = ['id', 'comment', 'author', 'created_at']

    def create(self, validated_data):
        return CommentReply.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance