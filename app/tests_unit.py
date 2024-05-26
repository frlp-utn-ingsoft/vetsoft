from datetime import date
from django.test import TestCase
from app.models import Client, Medicine, Pet


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

class PetModelTest(TestCase, ):
    def test_can_create_and_get_pet(self):
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        Pet.save_pet(
            {
                "name": "Loki",
                "breed": "Border Collie",
                "birthday": date(2024,5,5),
                "weight": 10,
                "client":1
            }
        )
        pets = Pet.objects.all()
        self.assertEqual(len(pets), 1)

        self.assertEqual(pets[0].name, "Loki")
        self.assertEqual(pets[0].breed, "Border Collie")
        self.assertEqual(pets[0].birthday, date(2024,5,5))
        self.assertEqual(pets[0].weight, 10)
        self.assertEqual(pets[0].client, Client.objects.get(pk=1))

class MedicineModelTest(TestCase):
    def test_can_create_and_get_medicine(self):
        Medicine.save_medicine(
            {
                "name": "ibuprofeno",
                "description": "analgesico",
                "dose": "4",
            }
        )
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "ibuprofeno")
        self.assertEqual(medicines[0].description, "analgesico")
        self.assertEqual(medicines[0].dose, 4)

    def test_can_update_medicine(self):
        Medicine.save_medicine(
            {
                "name": "ibuprofeno",
                "description": "analgesico",
                "dose": "4",
            }
        )
        medicine = Medicine.objects.get(pk=1)

        self.assertEqual(medicine.description, "analgesico")

        medicine.update_medicine({"description": "analgesico"})

        medicine_updated = Medicine.objects.get(pk=1)

        self.assertEqual(medicine_updated.description, "analgesico")

    def test_update_medicine_with_error(self):
        Medicine.save_medicine(
            {
                "name": "ibuprofeno",
                "description": "analgesico",
                "dose": "4",
            }
        )
        medicine = Medicine.objects.get(pk=1)

        self.assertEqual(medicine.description, "analgesico")

        medicine.update_medicine({"description": ""})

        medicine_updated = Medicine.objects.get(pk=1)

        self.assertEqual(medicine_updated.description, "analgesico")