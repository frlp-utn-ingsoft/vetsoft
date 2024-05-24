from django.test import TestCase
from app.models import Client, Medicine


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