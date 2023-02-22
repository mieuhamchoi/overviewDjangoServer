from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    numberPhone = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    sex = models.BooleanField(default=True)