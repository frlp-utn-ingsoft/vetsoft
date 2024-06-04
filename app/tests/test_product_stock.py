from django.test import TestCase

from app.models import Product


class ProductStockTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(name="Test Product", type="Type A", price=10.0, stock=100)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.type, "Type A")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.stock, 100)

    def test_increase_stock(self):
        product = Product.objects.create(name="Test Product", type="Type A", price=10.0, stock=100)
        product.stock += 10
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.stock, 110)

    def test_decrease_stock(self):
        product = Product.objects.create(name="Test Product", type="Type A", price=10.0, stock=100)
        product.stock -= 10
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.stock, 90)
        product.stock = 0
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.stock, 0)
