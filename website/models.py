from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL(), null=True, related_name='my_apps')

    def __str__(self):
        return f'Project {self.id} {self.name}'

    class Meta:
        verbose_name_plural = 'My Projects'
        ordering = ['name']