from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.SmallIntegerField()
    age = models.SmallIntegerField()
    operation = models.CharField(max_length=20)