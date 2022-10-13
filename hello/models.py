from django.db import models


class Friends(models.Model):
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    available = models.BooleanField()
    friend = models.CharField(max_length=255, null=True)


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
