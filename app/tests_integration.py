from django.shortcuts import reverse
from django.test import TestCase

from app.models import Medicine, Product, Provider, Vet

class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")



# class ClientsTest(TestCase):
#     def test_repo_use_repo_template(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_repo_display_all_clients(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_form_use_form_template(self):
#         response = self.client.get(reverse("clients_form"))
#         self.assertTemplateUsed(response, "clients/form.html")

#     def test_can_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             },
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#         self.assertRedirects(response, reverse("clients_repo"))

#     def test_validation_errors_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={},
#         )

#         self.assertContains(response, "Por favor ingrese un nombre")
#         self.assertContains(response, "Por favor ingrese un teléfono")
#         self.assertContains(response, "Por favor ingrese un email")

#     def test_should_response_with_404_status_if_client_doesnt_exists(self):
#         response = self.client.get(reverse("clients_edit", kwargs={"id": 100}))
#         self.assertEqual(response.status_code, 404)

#     def test_validation_invalid_email(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75",
#             },
#         )

#         self.assertContains(response, "Por favor ingrese un email valido")
    
class ClientsTest(TestCase):
    
    def test_validation_invalid_name(self):
            response = self.client.post(
                reverse("clients_form"),
                data={
                    "name": "1234$#%",
                    "phone": "22165438",
                    "address": "1 y 62",
                    "email": "tomasbret@hotmail.com",
                },
            )
            self.assertContains(response, "El nombre solo puede contener letras y espacios")

# class ClientsTest(TestCase):
#     def test_repo_use_repo_template(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_repo_display_all_clients(self):
#         response = self.client.get(reverse("clients_repo"))
#         self.assertTemplateUsed(response, "clients/repository.html")

#     def test_form_use_form_template(self):
#         response = self.client.get(reverse("clients_form"))
#         self.assertTemplateUsed(response, "clients/form.html")

#     def test_can_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             },
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#         self.assertRedirects(response, reverse("clients_repo"))

#     def test_validation_errors_create_client(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={},
#         )

#         self.assertContains(response, "Por favor ingrese un nombre")
#         self.assertContains(response, "Por favor ingrese un teléfono")
#         self.assertContains(response, "Por favor ingrese un email")

#     def test_should_response_with_404_status_if_client_doesnt_exists(self):
#         response = self.client.get(reverse("clients_edit", kwargs={"id": 100}))
#         self.assertEqual(response.status_code, 404)

#     def test_validation_invalid_email(self):
#         response = self.client.post(
#             reverse("clients_form"),
#             data={
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75",
#             },
#         )

#         self.assertContains(response, "Por favor ingrese un email valido")


    # def test_edit_user_with_valid_data(self):
    #     client = Client.objects.create(
    #         name="Juan Sebastián Veron",
    #         address="13 y 44",
    #         phone="221555232",
    #         email="brujita75@hotmail.com",
    #     )

    #     response = self.client.post(
    #         reverse("clients_form"),
    #         data={
    #             "id": client.id,
    #             "name": "Guido Carrillo",
    #         },
    #     )

    #     # redirect after post
    #     self.assertEqual(response.status_code, 302)

    #     editedClient = Client.objects.get(pk=client.id)
    #     self.assertEqual(editedClient.name, "Guido Carrillo")
    #     self.assertEqual(editedClient.phone, client.phone)
    #     self.assertEqual(editedClient.address, client.address)
    #     self.assertEqual(editedClient.email, client.email)


class MedicinesTest(TestCase):
    def test_can_create_medicine(self):
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "6",
            },
        )
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "Amoxicilina")
        self.assertEqual(medicines[0].description, "Antibiotico de amplio espectro")
        self.assertEqual(medicines[0].dose, 6)

        self.assertRedirects(response, reverse("medicines_repo"))

    def test_update_medicine_with_invalid_dose_zero(self):
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "0",
            },
        )
        self.assertContains(response, "La dosis debe estar entre 1 a 10")

    def test_update_medicine_with_invalide_dose(self):
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "11",
            },
        )
        self.assertContains(response, "La dosis debe estar entre 1 a 10")

    def test_update_medicine_with_invalid_dose_negative(self):
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "-5",
            },
        )
        self.assertContains(response, "La dosis debe ser un número entero positivo")


# cambios para actividad 3 punto 5 de TEST



class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

class ProviderTest(TestCase):
    def test_can_create_provider_with_address(self):
        response = self.client.post(
            reverse("providers_form"),
            data={
                "name": "Pepe Gonzales",
                "email": "pepe@hotmail.com",
                "address": "7 entre 13 y 44",
            },
        )
        provider = Provider.objects.first()

        self.assertEqual(provider.name, "Pepe Gonzales")
        self.assertEqual(provider.email, "pepe@hotmail.com")
        self.assertEqual(provider.address, "7 entre 13 y 44")

        self.assertRedirects(response, reverse("providers_repo"))

    def test_validation_errors_create_provider_without_address(self):
        response = self.client.post(
            reverse("providers_form"),
            data={
                "name": "Pepe Gonzales",
                "email": "pepe@hotmail.com",
                # No se proporciona la dirección
            },
        )

        self.assertContains(response, "Por favor ingrese una dirección")

# Test de Veterinario
class VetsTest(TestCase):
    def test_can_create_vet(self):
            response = self.client.post(
                reverse("vets_form"),
                data={
                    "name": "Joaquin Munos",
                    "phone": "22165438",
                    "address": "20 y 60",
                    "email": "joaquin10@hotmail.com",
                    "especialidad": "general",
                },
            )
            vets = Vet.objects.all()
            self.assertEqual(len(vets), 1)

            self.assertEqual(vets[0].name, "Joaquin Munos")
            self.assertEqual(vets[0].phone, "22165438")
            self.assertEqual(vets[0].address, "20 y 60")
            self.assertEqual(vets[0].email, "joaquin10@hotmail.com")
            self.assertEqual(vets[0].speciality, "general")

            self.assertRedirects(response, reverse("vets_repo"))

    def test_validation_invalid_especialidad(self):
            response = self.client.post(
                reverse("vets_form"),
                data={
                    "name": "Joaquin Munos",
                    "phone": "22165438",
                    "address": "20 y 60",
                    "email": "joaquin10@hotmail.com",
                    "especialidad": "",
                },
            )

            self.assertContains(response, "Por favor seleccione una especialidad")

class ProductsTest(TestCase):
    def test_can_create_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 8,
            },
        )
        products = Product.objects.all()
        self.assertEqual(len(products), 1)

        self.assertEqual(products[0].name, "NombreProducto")
        self.assertEqual(products[0].type, "TipoProducto")
        self.assertEqual(products[0].price, 8)

        self.assertRedirects(response, reverse("products_repo"))

    def test_create_product_negative_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": -8,
            },
        )
        self.assertContains(response, "El precio debe ser mayor a cero")
        
    def test_create_product_no_product(self):
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "NombreProducto",
                "type": "TipoProducto",
                "price": 0,
            },
        )
        self.assertContains(response, "El precio debe ser mayor a cero")



# agrego test intregacion punto 5 actividad 3


# class PetIntegrationTest(TestCase):
#     def setUp(self):
#         # Crea un cliente para ser el dueño de la mascota
#         self.client_obj = Client.objects.create(
#             name="Test Client", phone="221555232", email="test@test.com", address="13 y 44")

#         # Crea un cliente para enviar solicitudes HTTP
#         self.http_client = Client()

#     def test_create_pet(self):
#         # # Define la URL y los datos que se enviarán en la solicitud
#         # # Reemplaza 'create_pet' con la URL de tu vista
#         # url = reverse('pets_form')
#         # data = {
#         #     'name': 'Test Pet',
#         #     'breed': Breed.DOG,
#         #     'birthday': '2022-01-01',
#         #     'owner': self.client_obj.id
#         # }

#         response = self.client.post(
#             reverse("pets_form"),
#             data={
#                 "name": "Fido",
#                 "breed": Breed.DOG,
#                 "birthday": "2022-01-01",
#                 'owner': self.client_obj.id
#             },
#         )

#         # # Envía una solicitud POST a la vista
#         # response = self.http_client.post(url, data)

#         # Comprueba que la respuesta tenga un código de estado 200
#         # self.assertEqual(response.status_code, 200)

#         # Comprueba que la mascota se haya creado en la base de datos
#         # pet = Pet.objects.filter(name='Test Pet')
#         # self.assertTrue(pet.exists())
#         # self.assertEqual(pet.first().breed, Breed.DOG)
