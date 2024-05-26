from django.test import TestCase
from app.models import Pet
from datetime import datetime, timedelta

class PetModelTest(TestCase):

    def test_create_pet(self):
        pet = Pet.objects.create(name="Test Pet", breed="Test Breed", birthday=datetime.strptime("2024-05-06", "%Y-%m-%d").date())
        self.assertEqual(pet.name, "Test Pet")
        self.assertEqual(pet.breed, "Test Breed")
        self.assertEqual(pet.birthday, datetime.strptime("2024-05-06", "%Y-%m-%d").date())

    def test_validate_birthday_date_less_than_today (self):
        pet_birthday = datetime.strptime("2024-05-06", "%Y-%m-%d").date()
        if pet_birthday > datetime.now().date():
            raise ValueError("La fecha de cumpleaños no puede ser mayor al dia actual.")
        
        pet = Pet.objects.create(name="Test Pet", breed="Test Breed", birthday=pet_birthday)
        self.assertEqual(pet.name, "Test Pet")
        self.assertEqual(pet.breed, "Test Breed")
        self.assertEqual(pet.birthday, pet_birthday)
        self.assertTrue(pet.birthday < datetime.now().date(), "La fecha de cumpleaños no puede ser mayor al dia actual.")

    def test_validate_birthday_date_more_than_today (self):
        hoy = datetime.now().date()
        day = hoy + timedelta(days=1)
        pet = Pet.objects.create(name="Test Pet", breed="Test Breed", birthday=day)
        self.assertEqual(pet.name, "Test Pet")
        self.assertEqual(pet.breed, "Test Breed")
        self.assertEqual(pet.birthday, day)
        self.assertFalse(pet.birthday < datetime.now().date(), "La fecha de cumpleaños no puede ser mayor al dia actual.")