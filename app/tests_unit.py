from django.test import TestCase
from app.models import Client, Product, Pet
from datetime import date, timedelta


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
    def test_can_create_and_get_product_with_stock(self):
        Product.save_product(
            {
                "name": "Lavandina",
                "type": "Limpieza",
                "price": "100",
                "stock": "50",
            }
        )
        products = Product.objects.all()
        self.assertEqual(len(products), 1)

        self.assertEqual(products[0].name, "Lavandina")
        self.assertEqual(products[0].type, "Limpieza")
        self.assertEqual(products[0].price, 100.0)
        self.assertEqual(products[0].stock, 50)

    def test_can_update_product_stock(self):
        Product.save_product(
            {
                "name": "Lavandina",
                "type": "Limpieza",
                "price": "100",
                "stock": "50",
            }
        )
        product = Product.objects.get(pk=1)
        self.assertEqual(product.stock, 50)
        product.update_product({"stock":"75"})
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.stock, 75)
        
    def test_update_product_stock_with_error_negative_value(self):
        Product.save_product(
            {
                "name": "Lavandina",
                "type": "Limpieza",
                "price": "100",
                "stock": "50",
            }
        )
        product = Product.objects.get(pk=1)
        self.assertEqual(product.stock, 50)
        product.update_product({"stock":"-75"})
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.stock, 50)
        
    def test_update_product_stock_with_error_string_value(self):
        Product.save_product(
            {
                "name": "Lavandina",
                "type": "Limpieza",
                "price": "100",
                "stock": "50",
            }
        )
        product = Product.objects.get(pk=1)
        self.assertEqual(product.stock, 50)
        product.update_product({"stock":"asd"})
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.stock, 50)
    
    def test_update_product_stock_with_error_empty_value(self):
        Product.save_product(
            {
                "name": "Lavandina",
                "type": "Limpieza",
                "price": "100",
                "stock": "50",
            }
        )
        product = Product.objects.get(pk=1)
        self.assertEqual(product.stock, 50)
        product.update_product({"stock":""})
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.stock, 50)

class PetModelTest(TestCase):
    def test_can_create_pet_with_breed_options(self):
        past_birthday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        Pet.save_pet(
            {
                "name": "Benita",
                "breed": "Perro",
                "birthday": past_birthday,
            }
        )

        pets = Pet.objects.all()
        self.assertEqual(len(pets), 1)
        self.assertEqual(pets[0].name, "Benita")
        self.assertEqual(pets[0].breed, "Perro")
        self.assertEqual(pets[0].birthday, date(2024,5,24))

    def test_can_update_pet_breed(self):
        past_birthday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        Pet.save_pet(
            {
                "name": "Benita",
                "breed": "Perro",
                "birthday": past_birthday,
            }
        )

        pet = Pet.objects.get(pk=1)
        self.assertEqual(pet.breed, "Perro")
        pet.update_pet({"breed": "Gato"})
        pet_updated = Pet.objects.get(pk=1)
        self.assertEqual(pet_updated.breed, "Gato")

    def test_update_pet_with_error(self):
        past_birthday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        Pet.save_pet(
            {
                "name": "Benita",
                "breed": "Perro",
                "birthday": past_birthday,
            }
        )

        pet = Pet.objects.get(pk=1)
        self.assertEqual(pet.breed, "Perro")
        pet.update_pet({"breed": ""})
        pet_updated = Pet.objects.get(pk=1)
        self.assertEqual(pet_updated.breed, "Perro")