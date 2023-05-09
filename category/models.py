from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(null=True)
    description = models.CharField(max_length=1000)
