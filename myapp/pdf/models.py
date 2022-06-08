from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=1000)
    degree = models.CharField(max_length=1000)
    university = models.CharField(max_length=1000)
    achievement = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)

    
