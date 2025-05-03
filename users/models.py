from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username
    
class Viewer(CustomUser):
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username

