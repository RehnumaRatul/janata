from django import db
from django.db import models

# Create your models here.
class VisualData(models.Model):
   date=models.CharField(max_length=10000)
   trade_code=models.CharField(max_length=10000)
   high=models.CharField(max_length=10000)
   low=models.CharField(max_length=10000)
   open=models.CharField(max_length=10000)
   close=models.CharField(max_length=10000)
   volume=models.CharField(max_length=10000)

   def __str__(self):
        return f'{self.trade_code}-{self.volume}-{self.close}' 
      

  

   
