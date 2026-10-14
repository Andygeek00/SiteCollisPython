from django.db import models
from django.utils import timezone
import random
# Create your models here.

class Parcel(models.Model):
    tracking_number = models.CharField(max_length=11, unique=True)
    Adress_dep = models.CharField(max_length=100)
    Arr_dep = models.CharField(max_length=100)
    Weight = models.IntegerField()
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    # Generation du numero de suivi unique
    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = 'CM' + str(random.randint(168,999))
        super().save(*args, **kwargs)



    def __str__(self):
        return  f"Package N°{self.id} - {self.Weight}kg"


