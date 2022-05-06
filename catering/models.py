from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date_manufacture = models.DateTimeField()
    date_expiry_date = models.DateTimeField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name
        

