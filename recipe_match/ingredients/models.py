from django.db import models

# Create your models here.

class user_queries(models.Model):
    user_id = models.IntegerField()
    ingredients = models.CharField(max_length=40000)
    recipe_count = models.CharField(max_length=3)
