from django.db import models

# Create your models here.

class user_login(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    


class temp_url(models.Model):
    url = models.CharField(max_length=400)
    ip_add=models.CharField(max_length=255)