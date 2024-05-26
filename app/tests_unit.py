from django.test import TestCase
from app.models import Client, Provider


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

##### PROVEDOR #####

class ProviderModelTest(TestCase):
    def test_can_create_and_get_provider(self):
        Provider.save_provider(
            {
                "name": "Proveedor ABC",
                "phone": "123456789",
                "email": "proveedor@example.com",
                "address": "Calle 123",
                "floor_apartament": "Piso 3c",
            }
        )
        providers = Provider.objects.all()
        self.assertEqual(len(providers), 1)

        self.assertEqual(providers[0].name, "Proveedor ABC")
        self.assertEqual(providers[0].phone, "123456789")
        self.assertEqual(providers[0].email, "proveedor@example.com")
        self.assertEqual(providers[0].address, "Calle 123")
        self.assertEqual(providers[0].floor_apartament, "Piso 3c")

    def test_can_update_provider(self):
        Provider.save_provider(
            {
                "name": "Proveedor ABC",
                "phone": "123456789",
                "email": "proveedor@example.com",
                "address": "Calle 123",
                "floor_apartament": "Piso 3c",
            }
        )
        provider = Provider.objects.get(pk=1)

        self.assertEqual(provider.floor_apartament, "Piso 3c")

        provider.update_provider({"floor_apartament": "casa"})

        provider_updated = Provider.objects.get(pk=1)

        self.assertEqual(provider_updated.floor_apartament, "casa")

    def test_update_provider_with_error(self):
        Provider.save_provider(
            {
                "name": "Proveedor ABC",
                "phone": "123456789",
                "email": "proveedor@example.com",
                "address": "Calle 123",
                "floor_apartament": "Piso 3c",
            }
        )
        provider = Provider.objects.get(pk=1)

        self.assertEqual(provider.floor_apartament, "Piso 3c")

        provider.update_provider({"floor_apartament": ""})

        provider_updated = Provider.objects.get(pk=1)

        self.assertEqual(provider_updated.floor_apartament, "Piso 3c")
