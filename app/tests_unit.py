from .models import Pet, Client, Breed
from django.test import TestCase
from app.models import Pet, Client


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


# Agrego test unitarios para punto 5 actividad 3
# cambios por nueva rama  feature-agregaropcionesrazamascota
class PetModelTest(TestCase):
    def setUp(self):
        # Crea un cliente para ser el dueño de la mascota
        self.client = Client.objects.create(
            name="Test Client", phone="221555232", email="test@test.com", address="13 y 44")

    def test_create_pet(self):
        # Crea una nueva mascota
        pet = Pet.objects.create(
            name="Test Pet", breed=Breed.DOG, birthday="2022-01-01", owner=self.client)

        # Verifica que la mascota se haya guardado en la base de datos
        self.assertEqual(Pet.objects.count(), 1)
        self.assertEqual(Pet.objects.first(), pet)

    def test_breed_choices(self):
        # Crea mascotas con cada opción de raza
        pet_dog = Pet.objects.create(
            name="Dog Pet", breed=Breed.DOG, birthday="2022-01-01", owner=self.client)
        pet_cat = Pet.objects.create(
            name="Cat Pet", breed=Breed.CAT, birthday="2022-01-01", owner=self.client)
        pet_bird = Pet.objects.create(
            name="Bird Pet", breed=Breed.BIRD, birthday="2022-01-01", owner=self.client)

        # Verifica que las mascotas se hayan guardado con las razas correctas
        self.assertEqual(pet_dog.breed, Breed.DOG)
        self.assertEqual(pet_cat.breed, Breed.CAT)
        self.assertEqual(pet_bird.breed, Breed.BIRD)
