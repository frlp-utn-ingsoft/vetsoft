from django.test import TestCase
from app.models import Client, validate_pet
from datetime import date


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
    def test_birthday_today_date(self):

        today = date.today().isoformat()

        # Creo un setup
        pet_data = {
            "name": "Pepe",
            "breed": "Labrador",
            "birthday": today,
            "client": 1,
        }

        errors = validate_pet(pet_data)

        # Compruebo que hay error en el campo de birthday
        self.assertIn("birthday", errors)
        self.assertEqual(errors["birthday"], "La fecha de nacimiento no puede ser mayor o igual a la fecha actual")

    def test_birthday_past_dat(self):

        #Creo el setup
        pet_data = {
            "name": "Pepe",
            "breed": "Labrador",
            "birthday": "2020-01-01",
            "client": 1,
        }

        errors = validate_pet(pet_data)

        #Compruebo que no hay error en el campo de birthday
        self.assertNotIn("birthday", errors, "La fecha ingresada es correcta, no debe haber error")