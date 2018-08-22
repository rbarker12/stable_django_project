from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.TextField(null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    
