from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
