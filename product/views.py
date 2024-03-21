from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q
from .models import product,Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url="/login/"),name="dispatch")
class ProductView(ListView):
    model=product
    template_name="products.html"

class ProductDetailView(DetailView):
    model=product
    template_name='Products_detail.html'
    context_object_name='p'

def field_lookup(request):
    #products=product.cm.all().filter(Q(product_price__lt="900")& Q(product_name__icontains="dog"))
   # products=product.cm.all().filter(Q(id=6) | Q(id=7))
    products=product.cm.all().filter(~Q(product_Brand="PawsIndia"))



   # products=product.objects.all()
  # products=product.objects.filter(product_Brand="PawsIndia")
   #products=product.objects.filter(product_price_lt="600")
    #products=product.objects.filter(product_price_lte="600")
    #products=product.objects.filter(product_price_gt="600")
   # products=product.objects.filter(product_name_contains="Dog Collar")
    #products=Product.objects.filter(product_price_lte="600")
    return render(request,"productLookup.html",{"product":products})

class CategoryDetailView(DetailView):
    model=Category
    template_name="category.html"
    context_object_name="category"
    slug_field="slug"

