from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TwitterCredentails(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="credentials", on_delete=models.CASCADE)  #related_name="credentials" is used when you want to create index on foreign key; its like relation between tables
    access_token = models.CharField(max_length=100,null=True)
    access_secret = models.CharField(max_length=100,null=True)
    consumer_key = models.CharField(max_length=100,null=True)
    consumer_secret = models.CharField(max_length=100,null=True)
