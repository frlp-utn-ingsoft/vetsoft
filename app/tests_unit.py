from django.test import TestCase
from app.models import Client
from app.models import Pet

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
            "name": client.name,
            "phone": "221555233",
            "email": client.email
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


class petModelTest(TestCase):
    def test_can_create_and_get_pet(self):
        pet.save_pet(
            {
                "name": "Nami",
                "breed": "Siames",
                "birthday": '2020-05-22',
                "weight": "30",
            }
        )
        pets = pet.objects.all()
        self.assertEqual(len(pets), 1)

        self.assertEqual(pets[0].name, "Nami")
        self.assertEqual(pets[0].breed, "Siames")
        self.assertEqual(pets[0].birthday, '2020-05-22')
        self.assertEqual(pets[0].weight, "30")

    def test_can_update_pet(self):
        pet.save_pet(
            {
                "name": "Nami",
                "breed": "Siames",
                "birthday": '2020-05-22',
                "weight": "30",
            }
        )
        pet = pet.objects.get(pk=1)

        self.assertEqual(pet.weight, "30")

        pet.update_pet({
            "name": pet.name,
            "weight": "30",
            "breed": pet.breed
        })

        pet_updated = pet.objects.get(pk=1)

        self.assertEqual(pet_updated.weight, "30")

    def test_update_pet_with_error(self):
        pet.save_pet(
            {
                "name": "Nami",
                "breed": "Siames",
                "birthday": '2020-05-22',
                "weight": "-20",
            }
        )
        pet = pet.objects.get(pk=1)

        self.assertEqual(pet.weight, "-20")

        pet.update_pet({"phone": ""})

        pet_updated = pet.objects.get(pk=1)

        self.assertEqual(pet_updated.weight, "0")