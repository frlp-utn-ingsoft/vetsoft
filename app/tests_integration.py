from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client, Med


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


class MedicinesTest(TestCase):
    def test_repo_use_repo_template(self):
        response = self.client.get(reverse("meds_repo"))
        self.assertTemplateUsed(response, "meds/repository.html")

    def test_repo_display_all_medicines(self):
        response = self.client.get(reverse("meds_repo"))
        self.assertTemplateUsed(response, "meds/repository.html")

    def test_form_use_form_template(self):
        response = self.client.get(reverse("meds_form"))
        self.assertTemplateUsed(response, "meds/form.html")

    def test_can_create_medicine(self):
        response = self.client.post(
            reverse("meds_form"),
            data={
                "name": "Paracetamoldog",
                "desc": "Este medicamento es para vomitos caninos",
                "dose": 8,
            },
        )
        medicines = Med.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "Paracetamoldog")
        self.assertEqual(medicines[0].desc, "Este medicamento es para vomitos caninos")
        self.assertEqual(medicines[0].dose, 8)

        self.assertRedirects(response, reverse("meds_repo"))

    def test_validation_errors_create_medicine(self):
        response = self.client.post(
            reverse("meds_form"),
            data={},
        )

        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese una descripcion")
        self.assertContains(response, "Por favor ingrese una dosis")

    def test_should_response_with_404_status_if_medicine_doesnt_exists(self):
        response = self.client.get(reverse("meds_edit", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_validation_invalid_dosis(self):
        response = self.client.post(
            reverse("meds_form"),
            data={
                "name": "Paracetamoldog",
                "desc": "Este medicamento es para vomitos caninos",
                "dose": 18,
            },
        )

        self.assertContains(response, "La dosis debe estar entre 1 y 10")

    def test_edit_user_with_valid_data(self):
        medicine = Med.objects.create(
            name="Paracetamoldog",
            desc="Este medicamento es para vomitos caninos",
            dose=8,
        )

        response = self.client.post(
            reverse("meds_form"),
            data={
                "id": medicine.id,
                "name": "Ubuprofendog",
                "desc": "Este medicamento es para vomitos caninos",
                "dose": "8",
            },
        )

        # redirect after post
        self.assertEqual(response.status_code, 302)

        editedMedicine = Med.objects.get(pk=medicine.id)
        self.assertEqual(editedMedicine.name, "Ubuprofendog")
        self.assertEqual(editedMedicine.desc, medicine.desc)
        self.assertEqual(editedMedicine.dose, medicine.dose)

