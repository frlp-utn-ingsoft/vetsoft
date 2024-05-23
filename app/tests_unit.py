from django.test import TestCase
from app.models import Client, Vet, Speciality


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

class VetModelTest(TestCase):
    def test_can_create_and_get_vet(self):
        speciality = "Urgencias"
        self.assertTrue(self.is_valid_speciality(speciality))
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "221555232",
                "speciality": speciality,
            }
        )
        vets = Vet.objects.all()
        self.assertEqual(len(vets), 1)

        self.assertEqual(vets[0].name, "Juan Sebastian Veron")
        self.assertEqual(vets[0].email, "brujita75@hotmail.com")
        self.assertEqual(vets[0].phone, "221555232")
        self.assertEqual(vets[0].speciality, "Urgencias")

    def test_can_update_vet(self):
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "221555232",
                "speciality": "Urgencias",
            }
        )
        vet = Vet.objects.get(pk=1)

        self.assertEqual(vet.phone, "221555232")

        vet.update_vet({
            "name": "Juan Sebastian Veron",
            "email": "brujita75@hotmail.com",
            "phone": "221555233",
            "speciality": "Urgencias",
            })

        vet_updated = Vet.objects.get(pk=1)

        self.assertEqual(vet_updated.phone, "221555233")

    def test_update_vet_with_error(self):
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "221555232",
                "speciality": "Urgencias",
            }
        )
        vet = Vet.objects.get(pk=1)

        self.assertEqual(vet.phone, "221555232")

        vet.update_vet({"phone": ""})

        vet_updated = Vet.objects.get(pk=1)

        self.assertEqual(vet_updated.phone, "221555232")

    def is_valid_speciality(self, speciality):
        return speciality in [choice.value for choice in Speciality]
