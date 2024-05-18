from django.test import TestCase
from app.models import Client, validate_pet


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




class PetModelTest(TestCase):
    def test_weight_greater_than_zero(self):
          # Crear una instancia de Mascota con un peso mayor a cero
        mascota_data = {
            "name": "Fido",
            "breed": 2,
            "birthday": "2020-01-01",
            "weight": 10
        }
        errors = validate_pet(mascota_data)
        # verifica que no hay error en el peso
        self.assertNotIn("weight", errors, "No debe haber un error de peso cuando es mayor a cero")



    def weight_test_less_than_zero(self):
        # Crear una instancia de Mascota con un peso menor a cero
        mascota_data: dict ={
            "name": "Roma",
            "breed": 1,
            "birthday": "2021-01-01",
            "weight": -2
        }
       
        errors= validate_pet(mascota_data)
        #  verifica que la respuesta del error sea correcta
        self.assertEqual(errors["weight"], "El peso debe ser un número mayor a cero")
