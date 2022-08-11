from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=300)