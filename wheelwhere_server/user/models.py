from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    cell_phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
