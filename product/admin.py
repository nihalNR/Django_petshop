from django.contrib import admin
from .models import product,Category

# Register your models here.

@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_price','product_Brand','category')

#admin.site.register(product,productadmin)
    
    
@admin.register(Category)
class productadmin(admin.ModelAdmin):
    list_display=('id','category_name','slug')