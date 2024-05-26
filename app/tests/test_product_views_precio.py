from django.test import TestCase
from django.urls import reverse
from app.models import Product
from django.contrib.messages import get_messages

class ProductPrecioTest(TestCase):

    def test_validatePrecioMenor(self):
        product = Product.objects.create(name="Producto1", type="Tipo1", price=-15, stock=5)
        url = reverse('products_form')
        
        response = self.client.post(url, {'product_id': product.id})

        product.refresh_from_db()
        self.assertEqual(product.price, 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Precio menor o igual a 0")


    def test_validatePrecioMayor(self):
        product = Product.objects.create(name="Producto1", type="Tipo1", price=15, stock=5)
        url = reverse('products_form')
        
        response = self.client.post(url, {'product_id': product.id})

        product.refresh_from_db()
        self.assertEqual(product.price, 1)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)
