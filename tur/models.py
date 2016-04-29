from django.db import models

class cuenta(models.Model):
    usuario = models.CharField(max_length=150)
    password = models.CharField(max_length=150)