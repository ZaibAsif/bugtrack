from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from projects.models import Project


class Issue(models.Model):
    STATUS_CHOICES = [
        ('open','Open'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed'),
        ('reopened','Reopened')
    ]
    PRIORITY_CHOICES = [('low','Low'), ('medium','Medium'), ('high','High')]
    SEVERITY_CHOICES = [('minor','Minor'), ('major','Major'), ('critical','Critical')]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reported_issues'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='minor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_replies')
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
