from django.test import TestCase
from django.test import Client  # esto lo agrego para mi test
from django.shortcuts import reverse
from app.models import Client, Pet, Breed  # agregue pet para mis test

# cambios para actividad 3 punto 5 de TEST


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

########################### SEPARADOR ###################################
#########################################################################

# agrego test intregacion punto 5 actividad 3


class PetIntegrationTest(TestCase):
    def setUp(self):
        # Crea un cliente para ser el dueño de la mascota
        self.client_obj = Client.objects.create(
            name="Test Client", phone="221555232", email="test@test.com", address="13 y 44")

        # Crea un cliente para enviar solicitudes HTTP
        self.http_client = Client()

    def test_create_pet(self):
        # # Define la URL y los datos que se enviarán en la solicitud
        # # Reemplaza 'create_pet' con la URL de tu vista
        # url = reverse('pets_form')
        # data = {
        #     'name': 'Test Pet',
        #     'breed': Breed.DOG,
        #     'birthday': '2022-01-01',
        #     'owner': self.client_obj.id
        # }

        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "Fido",
                "breed": Breed.DOG,
                "birthday": "2022-01-01",
                'owner': self.client_obj.id
            },
        )

        # # Envía una solicitud POST a la vista
        # response = self.http_client.post(url, data)

        # Comprueba que la respuesta tenga un código de estado 200
        # self.assertEqual(response.status_code, 200)

        # Comprueba que la mascota se haya creado en la base de datos
        # pet = Pet.objects.filter(name='Test Pet')
        # self.assertTrue(pet.exists())
        # self.assertEqual(pet.first().breed, Breed.DOG)
