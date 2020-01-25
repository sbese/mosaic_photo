from django.db import models


class Pic(models.Model):
    url = models.TextField(unique=True)
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
