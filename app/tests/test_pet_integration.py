from django.test import TestCase
from django.urls import reverse
from app.models import Pet
from datetime import datetime, timedelta

class PetIntegrationTest(TestCase):

    def test_pet_form_empty_pet_view(self):
        hoy = datetime.now().date()
        day = hoy + timedelta(days=1)
        response = self.client.post(
            reverse("pets_form"),
            data={
                "name": "",
                "breed": "",
                "birthday": ""
            }
        )
        self.assertContains(response, "Por favor ingrese una fecha")
        self.assertContains(response, "Por favor ingrese un nombre")
        self.assertContains(response, "Por favor ingrese la raza")