from django.test import TestCase
from app.models import Client, validate_product


class ClientModelTest(TestCase):
    def test_can_create_and_get_client(self):
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        self.assertEqual(clients[0].name, "Juan Sebastian Veron")
        self.assertEqual(clients[0].phone, "221555232")
        self.assertEqual(clients[0].address, "13 y 44")
        self.assertEqual(clients[0].email, "brujita75@hotmail.com")

    def test_can_update_client(self):
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        client = Client.objects.get(pk=1)

        self.assertEqual(client.phone, "221555232")

        client.update_client({
            "name": "Juan Sebastian Veron",
            "phone": "221555233",
            "address": "13 y 44",
            "email": "brujita75@hotmail.com",
            })

        client_updated = Client.objects.get(pk=1)

        self.assertEqual(client_updated.phone, "221555233")

    def test_update_client_with_error(self):
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        client = Client.objects.get(pk=1)

        self.assertEqual(client.phone, "221555232")

        client.update_client({"phone": ""})

        client_updated = Client.objects.get(pk=1)

        self.assertEqual(client_updated.phone, "221555232")


class TestValidateProduct(TestCase):

    def test_valid_price(self):
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "100"
        }
        errors = validate_product(data)
        self.assertNotIn("price", errors)
    
    def test_price_equal_zero(self):
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "0"
        }
        errors = validate_product(data)
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "Por favor ingrese un precio mayor a cero")

    def test_price_missing(self):
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": ""
        }
        errors = validate_product(data)
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "Por favor ingrese un precio")
