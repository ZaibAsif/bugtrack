from django.db import models
from django.conf import settings

STATUS_CHOICES = (
    ('bug', 'Bug'),
    ('development', 'Development'),
    ('qa', 'Qa'),
    ('review', 'Review'),
    ('deploy', 'Deploy'),
)    
class Project(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='bug')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='ProjectRole',
        related_name='projects_project_set',
    )
class ProjectRole(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Project Manager'),
        ('developer', 'Developer'),
        ('tester', 'Tester'),
        ('reporter', 'Reporter'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
