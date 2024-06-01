from django.test import TestCase
from django.urls import reverse
from app.models import Pet
from datetime import datetime, timedelta
from django.contrib.messages import get_messages


class PetViewsTest(TestCase):

    def test_pet_form_bd_today_view(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        
        response = self.client.post(
            reverse("pets_form"),
            {
                "name": "Test Pet",
                "breed": "Test Breed",
                "birthday": today
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)



    def test_pet_form_bd_tomorrow_view(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        response = self.client.post(
            reverse("pets_form"),
            {   
                "name": "Test Pet",
                "breed": "Test Breed",
                "birthday": tomorrow
            }
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("'birthday': 'La fecha de cumpleaños no puede ser mayor al dia actual'", str(messages[0]))

    def test_empty_pet_form_view(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        response = self.client.post(
            reverse("pets_form"),
            {   
                "name": "",
                "breed": "",
                "birthday": ""
            }
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("'birthday': 'Por favor ingrese una fecha'", str(messages))
        self.assertIn("'name': 'Por favor ingrese un nombre'", str(messages))
        self.assertIn("'breed': 'Por favor ingrese la raza'", str(messages))
