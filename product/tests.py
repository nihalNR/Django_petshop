from django.test import TestCase
from .models import product

# Create your tests here.

class ProductTest(TestCase):
    def setUp(self):
        self.products=product.pm.create(product_name="TestProduct",
                          product_description="Product has been created for testing",
                          product_Brand="TestBrand",
                          product_price=399)
        
    def test_create_product(self):
        products=product.pm.get(product_name="TestProduct")
        self.assertEqual(products.id,self.products.id)

    def test_update_product(self):
        products=product.pm.get(product_name="TestProduct")
        products.product_price=500
        products.save()

        self.assertNotEqual(products.product_price,self.products.product_price)

    def test_fetch_product(self):
        products=product.pm.all()
        count=len(products)
        self.assertGreater(count,0)