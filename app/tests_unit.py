from django.test import TestCase
from app.models import Client, Product, Provider, Vet

class ProviderModelTest(TestCase):
    def test_can_create_and_get_provider(self):
        Provider.save_provider(
            {
                "name": "Pepe Gonzales",
                "email": "pepe@hotmail.com",
                "address": "7 entre 13 y 44",
            }
        )
        provider = Provider.objects.all()
        
        self.assertEqual(len(provider), 1)
        self.assertEqual(provider[0].name, "Pepe Gonzales")
        self.assertEqual(provider[0].email, "pepe@hotmail.com")
        self.assertEqual(provider[0].address, "7 entre 13 y 44")

# class ClientModelTest(TestCase):
#     def test_can_create_and_get_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#     def test_can_update_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": "221555233"})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555233")

#     def test_update_client_with_error(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": ""})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555232")

#Test de veterinario
class VetModelTest(TestCase):
    def test_can_create_and_get_vet(self):
        Vet.save_vet(
            {
                "name": "Tomas Sbert",
                "phone": "2314557290",
                "address": "La Plata 43",
                "email": "tomasbret_dx@hotmail.com",
                "especialidad": "general",
            }
        )

        vets = Vet.objects.all()

        self.assertEqual(len(vets), 1)

        self.assertEqual(vets[0].name, "Tomas Sbert")
        self.assertEqual(vets[0].phone, "2314557290")
        self.assertEqual(vets[0].address, "La Plata 43")
        self.assertEqual(vets[0].email, "tomasbret_dx@hotmail.com")
        self.assertEqual(vets[0].speciality, "general")

    def test_can_delete_vet(self):
        vet = Vet.objects.create(
            name="Tomas Sbert",
            phone="2314557290",
            address="La Plata 43",
            email="tomasbret_dx@hotmail.com",
            speciality="general"
        )

        # Eliminar el veterinario
        vet.delete()

        # Verificar que el veterinario haya sido eliminado
        vets = Vet.objects.all()
        self.assertEqual(len(vets), 0)

        
class ProductModelTest(TestCase):
    def test_can_create_and_get_product(self):
        Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 8,
            }
        )

        products = Product.objects.all()
        self.assertEqual(len(products), 1)

        self.assertEqual(products[0].name, "NombreProducto")
        self.assertEqual(products[0].type, "TipoProducto")
        self.assertEqual(products[0].price, 8)

    def test_create_product_with_negative_product(self):
        Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": -8,
            }
        )

        products = Product.objects.all()
        self.assertEqual(len(products), 0)


    def test_create_product_with_no_product(self):
        Product.save_product(
            {
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 0,
            }
        )

        products = Product.objects.all()
        self.assertEqual(len(products), 0)
