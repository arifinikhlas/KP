from django.db import models

class UserTop5(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
