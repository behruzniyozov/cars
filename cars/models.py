from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


class Car(models.Model):
    class GearType(models.TextChoices):
        MANUAL = 'M', 'Manual'
        AUTOMATIC = 'A', 'Automatic'
        HYBRID = 'H', 'Hybrid'
        ELECTRIC = 'E', 'Electric'

    name= models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    price= models.PositiveIntegerField(null=False, blank=False)
    year= models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)]) 
    image= models.ImageField(upload_to='cars/')
    distance_covered= models.PositiveIntegerField(validators=[MinValueValidator(0)])
    brand= models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    gear_type= models.CharField(max_length=1, choices=GearType.choices)
    

    def __str__(self):
        return self.name
    

class Brend(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    logo= models.ImageField(upload_to='Logos/', null=True, blank=True)
    def __str__(self):
        return self.name