from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    vacancy = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    stipend= models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    last_date=models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title + ' | ' +str(self.author)