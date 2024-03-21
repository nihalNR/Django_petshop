from django.db import models
from . import managers as m
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=12)
    slug=AutoSlugField(populate_from="category_name")

    def __str__(self):
        return self.category_name


class product(models.Model):
    product_name=models.CharField(max_length=100,default='ProductName')
    product_description=models.TextField(default='Description')
    product_price=models.IntegerField(default=0)
    product_Brand=models.CharField(max_length=75,default='PawsIndia')
    product_picture=models.ImageField(upload_to="images/",default="")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    pm=models.Manager()
    cm=m.ProductManager()

    def __str__(self):
        return self.product_name