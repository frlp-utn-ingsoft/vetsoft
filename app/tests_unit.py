from django.test import TestCase
# from app.models import Client
from app.models import Medicine


# class ClientModelTest(TestCase):
#     def test_can_create_and_get_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         clients = Client.objects.all()
#         self.assertEqual(len(clients), 1)

#         self.assertEqual(clients[0].name, "Juan Sebastian Veron")
#         self.assertEqual(clients[0].phone, "221555232")
#         self.assertEqual(clients[0].address, "13 y 44")
#         self.assertEqual(clients[0].email, "brujita75@hotmail.com")

#     def test_can_update_client(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": "221555233"})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555233")

#     def test_update_client_with_error(self):
#         Client.save_client(
#             {
#                 "name": "Juan Sebastian Veron",
#                 "phone": "221555232",
#                 "address": "13 y 44",
#                 "email": "brujita75@hotmail.com",
#             }
#         )
#         client = Client.objects.get(pk=1)

#         self.assertEqual(client.phone, "221555232")

#         client.update_client({"phone": ""})

#         client_updated = Client.objects.get(pk=1)

#         self.assertEqual(client_updated.phone, "221555232")



class MedicineModelTest(TestCase):
    def test_can_create_and_get_medicine(self):
        success, errors = Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose": "6",
            }
        )
        self.assertTrue(success)
        self.assertIsNone(errors)
        
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)

        self.assertEqual(medicines[0].name, "Amoxicilina")
        self.assertEqual(medicines[0].description, "Antibiotico de amplio espectro")
        self.assertEqual(medicines[0].dose, 6)

    def test_update_medicine_with_invalid_dose_zero(self):
        Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"0",
            }
        )
        medicinas = Medicine.objects.all()
        self.assertEqual(len(medicinas), 0)

    def test_update_medicine_with_invalide_dose(self):
        Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"11",
            }
        )
        medicinas=Medicine.objects.all()
        self.assertEqual(len(medicinas),0)

    def test_update_medicine_with_invalid_dose_negative(self):
        Medicine.save_medicine(
            {
                "name": "Amoxicilina",
                "description": "Antibiotico de amplio espectro",
                "dose":"-5",
            }
        )
        medicinas = Medicine.objects.all()
        self.assertEqual(len(medicinas), 0)
    