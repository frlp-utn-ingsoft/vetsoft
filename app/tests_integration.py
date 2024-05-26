from datetime import date
from django.test import TestCase
from django.shortcuts import reverse
from app.models import Client, Medicine, Pet


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


class MedicineTest(TestCase):
    def test_repo_use_repo_template(self):
        response = self.client.get(reverse("medicine_repo"))
        self.assertTemplateUsed(response, "medicine/repository.html")

    def test_repo_display_all_medicines(self):
        response = self.client.get(reverse("medicine_repo"))
        self.assertTemplateUsed(response, "medicine/repository.html")

    def test_form_use_form_template(self):
        response = self.client.get(reverse("medicine_form"))
        self.assertTemplateUsed(response, "medicine/form.html")

    def test_can_create_medicine(self):
        response = self.client.post(
            reverse("medicine_form"),
            data={
                "name": "ibuprofeno",
                "description": "analgesico",
                "dose": "4",
            },
        )
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "ibuprofeno")
        self.assertEqual(medicines[0].description, "analgesico")
        self.assertEqual(medicines[0].dose, 4)

        self.assertRedirects(response, reverse("medicine_repo"))

    def test_validation_errors_create_medicie(self):
        response = self.client.post(
            reverse("medicine_form"),
            self.assertContains(response, "Por favor ingrese una descripcion")
        self.assertContains(response, "Por favor ingrese una dosis")

    def test_should_response_with_404_status_if_medicine_doesnt_exists(self):
        response = self.client.get(reverse("medicine_edit", kwargs={"id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_validation_invalid_dose(self):
        response = self.client.post(
            reverse("medicine_form"),
            data={
                "name": "ibuprofeno",
                "description": "analgesico",
                "dose": -1,
            },
        )

        self.assertContains(response, "Por favor ingrese una dosis")

    def test_edit_medicine_with_valid_data(self):
        medicine = Medicine.objects.create(
            name="ibuprofeno",
            description="analgesico",
            dose= 4,
        )

        response = self.client.post(
            reverse("medicine_form"),
            data={
                "id": medicine.id,
                "name": "ibuprofeno",
            },
        )

        # redirect after post
        self.assertEqual(response.status_code, 302)

        editedMedicine = Medicine.objects.get(pk=medicine.id)
        self.assertEqual(editedMedicine.name, "ibuprofeno")
        self.assertEqual(editedMedicine.description, medicine.description)
        self.assertEqual(editedMedicine.dose, medicine.dose)
 
          
 class PetsTest(TestCase):
    def test_can_create_pet(self):

        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )

        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "Loki",
                "breed": "Border Collie",
                "birthday": date(2024,5,5),
                "weight": 10,
                "client":1
            },
        )

        pets = Pet.objects.all()
        self.assertEqual(len(pets), 1)

        self.assertEqual(pets[0].name, "Loki")
        self.assertEqual(pets[0].breed, "Border Collie")
        self.assertEqual(pets[0].birthday, date(2024,5,5))
        self.assertEqual(pets[0].weight, 10)
        self.assertEqual(pets[0].client, Client.objects.get(pk=1))

        self.assertRedirects(response, reverse("pets_repo"))

    def test_validation_errors_create_pet(self):
        response = self.client.post(
            reverse("pets_form"),
            data={},
        )

        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese una raza")
        self.assertContains(response, "Por favor ingrese la fecha de cumpleaños")
        self.assertContains(response, "Por favor ingrese un peso")

    def test_validation_invalid_weight(self):
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "address": "13 y 44",
                "email": "brujita75@hotmail.com",
            }
        )
        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "Loki",
                "breed": "Border Collie",
                "birthday": date(2024,5,5),
                "weight": 0,
                "client":1
            },
        )
        self.assertContains(response, "Por favor ingrese un peso mayor que 0")
    