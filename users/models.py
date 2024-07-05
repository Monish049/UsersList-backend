from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=100)
