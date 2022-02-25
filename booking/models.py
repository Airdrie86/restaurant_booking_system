from django.db import models
from django

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
