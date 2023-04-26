from django.db import models
from django.core import validators
# Create your models here.
class Menu(models.Model):
    item=models.CharField(max_length=30,primary_key=True,)
   
    price=models.IntegerField(default=20)
    def __str__(self) -> str:
        return self.item
class Order(models.Model):
    date=models.DateField(auto_now=True)
    item=models.ForeignKey(Menu,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField(default=20)
    amount=models.BigIntegerField() 
    
class Report(models.Model):
    date=models.CharField(max_length=20)
    item=models.ForeignKey(Menu,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField(default=20)
    amount=models.BigIntegerField()