from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client


class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

class ClientsTest(TestCase):
    def test_repo_use_repo_template(self):
        response = self.client.get(reverse("clients_repo"))
        self.assertTemplateUsed(response, "clients/repository.html")

    def test_repo_display_all_clients(self):
        response = self.client.get(reverse("clients_repo"))
        self.assertTemplateUsed(response, "clients/repository.html")

    def test_form_use_form_template(self):
        response = self.client.get(reverse("clients_form"))
        self.assertTemplateUsed(response, "clients/form.html")

    def test_can_create_client(self):
        response = self.client.post(
            reverse("clients_form"),
            data={
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            },
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        self.assertEqual(clients[0].name, "Juan Sebastian Veron")
        self.assertEqual(clients[0].phone, "221555232")
        self.assertEqual(clients[0].address, "13 y 44")
        self.assertEqual(clients[0].email, "brujita75@hotmail.com")

        self.assertRedirects(response, reverse("clients_repo"))

    def test_validation_errors_create_client(self):
        response = self.client.post(
            reverse("clients_form"),
            data={},
        )

        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese un teléfono")
        self.assertContains(response, "Por favor ingrese un email")

    def test_should_response_with_404_status_if_client_doesnt_exists(self):
        response = self.client.get(reverse("clients_edit", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_validation_invalid_email(self):
        response = self.client.post(
            reverse("clients_form"),
            data={
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75",
            },
        )

        self.assertContains(response, "Por favor ingrese un email valido")

    def test_edit_user_with_valid_data(self):
        client = Client.objects.create(
            name="Juan Sebastián Veron",
            address="13 y 44",
            phone="221555232",
            email="brujita75@hotmail.com",
        )

        response = self.client.post(
            reverse("clients_form"),
            data={
                "id": client.id,
                "name": "Guido Carrillo",
            },
        )

        # redirect after post
        self.assertEqual(response.status_code, 302)

        editedClient = Client.objects.get(pk=client.id)
        self.assertEqual(editedClient.name, "Guido Carrillo")
        self.assertEqual(editedClient.phone, client.phone)
        self.assertEqual(editedClient.address, client.address)
        self.assertEqual(editedClient.email, client.email)

class PetsTest(TestCase):

    # verifica que se una la template correcta
    def test_form_use_form_template(self):
        response = self.client.get(reverse("pets_form"))
        self.assertTemplateUsed(response, "pets/form.html")
        
     # validar de que la raza no puede ser null
    def test_validation_errors_pet_breedless(self):
        response = self.client.post(
                reverse("pets_form"),
                data={
                    "name": "Posta",
                    "breed": "",
                    "birthday": "2021-10-10",
                    "weight": 180.05
                },
            )
        # Verifico si no tiene raza y muestra un mensaje de error
        self.assertContains(response, "Por favor seleccione una raza")

class ProductsTest(TestCase):
    def test_validation_invalid_price(self):
        # client es un objeto que proporciona Django para simular solicitudes HTTP en tus tests.
        response = self.client.post(
            reverse("products_form"),
            data={
                "name": "Paracetamol",
                "description": "Medicamento para el dolor",
                "price": 0,
            },
        )

        self.assertContains(response, "El precio debe ser mayor que cero")
        
class MedicinesTest(TestCase):
    def test_validation_invalid_dose(self):
        # client es un objeto que proporciona Django para simular solicitudes HTTP en tus tests.
        response = self.client.post(
            reverse("medicines_form"),
            data={
                "name": "Diclofenac",
                "description": "Calma el dolor muscular",
                "dose": 0,
            },
        )

        self.assertContains(response, "La dosis debe estar en un rango de 1 a 10")