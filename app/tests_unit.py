from django.forms import ValidationError
from django.test import TestCase
from app.models import Client, Medicine, Pet, Product

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

        client.update_client({"phone": "221555233"})

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

class ProductModelTest(TestCase):
    def test_invalid_price(self):
        result, errors = Product.save_product({
                "name": "Producto Invalido",
                "type": "Tipo",
                "price": -10.0,
            })
        self.assertEqual(result, False)
        self.assertDictEqual(errors, {'price': 'Los precios deben ser mayores que 0'})

    def test_valid_price(self):
        Product.save_product({
            "name": "Producto Valido",
            "type": "Tipo",
            "price": 10.0,
        })
        product = Product.objects.get(pk=1)
        self.assertEqual(product.price, 10.0)

class ProductModelTest(TestCase):
    def test_valid_price(self):
        result, errors = Product.save_product({
            "name": "Producto Valido",
            "type": "Tipo",
            "price": 10.0,
        })
        self.assertEqual(result, True)
        self.assertIsNone(errors)

    def test_invalid_price(self):
        result, errors = Product.save_product({
            "name": "Producto Invalido",
            "type": "Tipo",
            "price": -10.0,
        })
        self.assertEqual(result, False)
        self.assertDictEqual(errors, {'price': 'Los precios deben ser mayores que 0'})

class MedicineModelTest(TestCase):
    def test_invalid_dose(self):
        result, errors = Medicine.save_medicine({
            "name": "Medicina Invalida",
            "description": "Descripción",
            "dose": 0.5,
        })
        self.assertEqual(result, False)
        self.assertDictEqual(errors, {'dose': 'Las dosis deben estar entre 1 y 10'})

    def test_valid_dose(self):
        result, errors = Medicine.save_medicine({
            "name": "Medicina Valida",
            "description": "Descripción",
            "dose": 5.0,
        })
        self.assertEqual(result, True)
        self.assertIsNone(errors)

class PetModelTest(TestCase):
    def test_invalid_weight(self):
        result, errors = Pet.save_pet({
            "name": "Mascota Invalida",
            "breed": "Raza",
            "weight": -5.0,
            "birthday": "2024-05-20",
        })
        self.assertEqual(result, False)
        self.assertDictEqual(errors, {'weight': 'El peso debe ser mayor que 0'})

    def test_valid_weight(self):
        result, errors = Pet.save_pet({
            "name": "Mascota Valida",
            "breed": "Raza",
            "weight": 5.0,
            "birthday": "2024-05-20",
        })
        self.assertEqual(result, True)
        self.assertIsNone(errors)
