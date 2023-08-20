from django.db import models

# Create your models here.

class Video(models.Model):
    name=models.CharField(max_length=100)    
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.name   

class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=12)
    qualification=models.CharField(max_length=100)
    def __str__(self):

        return self


   







 