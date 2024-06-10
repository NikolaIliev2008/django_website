from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now_add=True)
