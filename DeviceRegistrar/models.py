
from django.db import models

# Create your models here.
class Entry(models.Model):
    Id = models.CharField(max_length=17,primary_key=True ,unique=True)
    DeviceType = models.CharField(max_length=20)
    DeviceVersion = models.CharField(max_length=20)
    DeviceLocation = models.CharField(max_length=50)
    PrimaryGroup = models.CharField(max_length=50)  # we want this field as nullable can be null  , NotRequired=True
    SecondaryGroup = models.CharField(max_length=50)  # we want this field as nullable can be null  , NotRequired=True
    LastContact = models.TimeField(auto_now=False,auto_now_add=False, null=True)
    Status = models.CharField(max_length=4 ,null=True)
    
    def __str__(self):
      return self.DeviceType


