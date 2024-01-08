from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    '''this image for user and we can see this'''
    image = models.ImageField(upload_to='users/%Y/%m/', blank=True,null=True)
    '''this bio for user and we can see this'''
    bio = models.TextField(max_length=255, blank=True,null=True)
