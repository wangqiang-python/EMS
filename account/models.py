from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    auto_code = models.CharField(max_length=20)
