from django.test import TestCase
from django.urls import reverse
from app.models import Pet
from datetime import datetime

class PetViewsTest(TestCase):

    def test_pet_form_view(self):
        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "Test Pet",
                "breed": "Test Breed",
                "birthday": datetime.strptime("2024-06-06", "%Y-%m-%d").date()
            }
        )
        self.assertContains(response, "Por favor ingrese una fecha")