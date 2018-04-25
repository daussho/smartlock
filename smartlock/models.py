from django.db import models


class Users(models.Model):
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=65)
    user_name = models.CharField(max_length=25)
    contact = models.CharField(max_length=25)


class Logs(models.Model):
    user_id = models.CharField(max_length=10)
    time = models.DateTimeField()