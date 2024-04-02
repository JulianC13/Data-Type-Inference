from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=100)
    Score = models.IntegerField()
    Birthdate = models.DateTimeField(auto_now_add=True)
    Grade =  models.CharField(max_length=10)
    def __str__(self):
        return self.name
    