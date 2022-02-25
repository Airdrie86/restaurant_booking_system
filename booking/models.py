from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    
    
