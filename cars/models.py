from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField
    
