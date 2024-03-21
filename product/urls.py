from django.contrib import admin
from django.urls import path
from .views import ProductView,ProductDetailView,field_lookup,CategoryDetailView

urlpatterns = [
    
    path('products/',ProductView.as_view()),
    path('products/<int:pk>',ProductDetailView.as_view(),name="productdetail"),
    path('product/',field_lookup),
    path('category/<slug:slug>',CategoryDetailView.as_view(),name="category")
    
]