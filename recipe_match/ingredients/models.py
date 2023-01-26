from django.db import models

# Create your models here.

class temp_url(models.Model):
    url = models.CharField(max_length=400)
    # ip_add=models.CharField(max_length=255)