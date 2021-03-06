from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.city + ' | ' + self.code

class Post(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    vacancy = models.IntegerField(default=0) 
    deadline = models.DateField()
    date = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    stipend= models.IntegerField(default=0) 
    skills = models.CharField(max_length=255)
    content = models.TextField(default="")
    location = models.ForeignKey(Location, blank=False, on_delete=models.CASCADE, related_name="intern")
    
    def __str__(self):
        return self.title + ' | ' + self.company
