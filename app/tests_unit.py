from django.test import TestCase
from app.models import Client
from .models import Provider


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


class ProviderModelTest(TestCase):
    
    def test_create_provider_with_address(self):
        # Datos de prueba
        provider_data = {
            "name": "Pedro Perez",
            "email": "PedroP012@hotmail.com",
            "address": "Calle 142 723"
        }

        # Crear proveedor
        success, errors = Provider.save_provider(provider_data)

        # Verificar que no hubo errores y que la creación fue exitosa
        self.assertTrue(success)
        self.assertIsNone(errors)

        # Recuperar el proveedor de la base de datos
        provider = Provider.objects.get(email="PedroP012@hotmail.com")

        # Verificar que los datos se guardaron correctamente
        self.assertEqual(provider.name, "Pedro Perez")
        self.assertEqual(provider.email, "PedroP012@hotmail.com")
        self.assertEqual(provider.address, "Calle 142 723")

    def test_update_provider_with_address(self):
        # Datos de prueba iniciales
        provider = Provider.objects.create(
            name="Proveedor Original",
            email="original@ejemplo.com",
            address="Dirección Original"
        )

        # Datos de prueba para actualización
        update_data = {
            "name": "Proveedor Actualizado",
            "email": "actualizado@ejemplo.com",
            "address": "Dirección Actualizada"
        }

        # Actualizar proveedor
        provider.update_provider(update_data)

        # Verificar que los datos se actualizaron correctamente
        self.assertEqual(provider.name, "Proveedor Actualizado")
        self.assertEqual(provider.email, "actualizado@ejemplo.com")
        self.assertEqual(provider.address, "Dirección Actualizada")