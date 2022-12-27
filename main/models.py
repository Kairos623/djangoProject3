from django.db import models

# Create your models here.

class Admin(models.Model):
    pass

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)