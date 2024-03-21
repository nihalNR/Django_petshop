from django.db import models

from django.db.models.query import QuerySet

class ProductManager(models.Manager):

   def get_queryset(self):
    #    return ProductQuerySet(self.model).getPawsIndia()
       return ProductQuerySet(self.model)
    
   def listed(self):
        return super().get_queryset().order_by('product_name')
    
   def sortByPrice(self):
        return super().get_queryset().order_by('product_price')
    
class ProductQuerySet(models.QuerySet):

    def getPawsIndia(self):
        return self.filter(product_Brand="PawsIndia")
    
    