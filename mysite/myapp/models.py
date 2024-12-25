from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
    monthly_expenses = models.IntegerField(default=0)
    monthly_income = models.IntegerField(default=0)
