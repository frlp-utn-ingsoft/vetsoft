from django.shortcuts import reverse
from django.test import TestCase

from app.models import Medicine, Product, Provider, Vet, Pet, Breed


class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


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
        self.assertContains(
            response, "El nombre solo puede contener letras y espacios")

########################### SEPARADOR ###################################
#########################################################################


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
        self.assertEqual(medicines[0].description,
                         "Antibiotico de amplio espectro")
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
        self.assertContains(
            response, "La dosis debe ser un número entero positivo")


########################### SEPARADOR ###################################
#########################################################################


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


########################### SEPARADOR ###################################
#########################################################################

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


########################### SEPARADOR ###################################
#########################################################################
class PetTest(TestCase):
    def test_can_create_pet(self):
        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "Pepito",
                "breed": Breed.DOG,
                "birthday": "2024-01-01",
            },
        )
        pets = Pet.objects.all()
        self.assertEqual(len(pets), 1)
        self.assertEqual(pets[0].name, "Pepito")
        self.assertEqual(pets[0].breed, Breed.DOG)
        self.assertEqual(pets[0].birthday.strftime("%Y-%m-%d"), "2024-01-01")
        self.assertRedirects(response, reverse("pets_repo"))
