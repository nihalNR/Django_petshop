from django.contrib import admin
from.models import Order,OrderItem

# Register your models here.

class orderItemInline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[orderItemInline]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
