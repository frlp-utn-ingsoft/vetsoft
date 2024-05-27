from django.test import TestCase
from app.models import Client, validate_pet, validate_product,validate_medicine, validate_pet
from datetime import date

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


# TEST DE PET
class PetModelTest(TestCase):
    def test_weight_greater_than_zero(self):
          # Crear una instancia de Mascota con un peso mayor a cero
        mascota_data = {
            "name": "Fido",
            "breed": 2,
            "birthday": "2020-01-01",
            "weight": 10
        }
        errors = validate_pet(mascota_data)
        # verifica que no hay error en el peso
        self.assertNotIn("weight", errors, "No debe haber un error de peso cuando es mayor a cero")



    def weight_test_less_than_zero(self):
        # Crear una instancia de Mascota con un peso menor a cero
        mascota_data: dict ={
            "name": "Roma",
            "breed": 1,
            "birthday": "2021-01-01",
            "weight": -2
        }
       
        errors= validate_pet(mascota_data)
        #  verifica que la respuesta del error sea correcta
        self.assertEqual(errors["weight"], "El peso debe ser un número mayor a cero")
        
    def test_birthday_today_date(self):

        today = date.today().isoformat()

        # Creo un setup
        pet_data = {
            "name": "Pepe",
            "breed": "Labrador",
            "birthday": today,
            "weight": 10,
            "client": 1,
        }

        errors = validate_pet(pet_data)

        # Compruebo que hay error en el campo de birthday
        self.assertIn("birthday", errors)
        self.assertEqual(errors["birthday"], "La fecha de nacimiento no puede ser mayor o igual a la fecha actual")

    def test_birthday_past_date(self):

        #Creo el setup
        pet_data = {
            "name": "Pepe",
            "breed": "Labrador",
            "birthday": "2020-01-01",
            "weight": 10,
            "client": 1,
        }

        errors = validate_pet(pet_data)

        #Compruebo que no hay error en el campo de birthday
        self.assertNotIn("birthday", errors, "La fecha ingresada es correcta, no debe haber error")

class MedicineModelTest(TestCase):
    def test_medicine_dose_validation_in_range_1_to_10(self):
        # Crear un diccionario con los datos del medicamento
        medicine_data = {
            "name": "Test Medicine",
            "description": "Test Description",
            "dose": -10 
        }

        # Llamar a la función de validación del medicamento
        errors = validate_medicine(medicine_data)

        # Comprobar que hay un error de validación en el campo 'dose'
        self.assertIn("dose", errors)
        self.assertEqual(errors["dose"], "La dosis debe estar en un rango de 1 a 10")

        # Probar con otra dosis inválida, superando el rango
        medicine_data["dose"] = 15
        errors = validate_medicine(medicine_data)

        # Comprobar que hay un error de validación en el campo 'dose'
        self.assertIn("dose", errors)
        self.assertEqual(errors["dose"], "La dosis debe estar en un rango de 1 a 10")

        # Probar con otra dosis válida, dentro el rango
        medicine_data["dose"] = 10
        errors = validate_medicine(medicine_data)

        # Comprobar que no hay errores de validación
        self.assertNotIn("dose", errors)

        # Probar con otra dosis válida, dentro el rango
        medicine_data["dose"] = 5
        errors = validate_medicine(medicine_data)

        # Comprobar que no hay errores de validación
        self.assertNotIn("dose", errors)

class ProductModelTest(TestCase):
    def test_price_greater_than_zero(self):
        # Crear un diccionario con los datos del producto
        product_data = {
            "name": "Test Product",
            "type": "Test Type",
            "price": -10 
        }

        # Llamar a la función de validación del producto
        errors = validate_product(product_data)

        # Comprobar que hay un error de validación en el campo 'price'
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "El precio debe ser mayor que cero")

        # Probar con un precio válido
        product_data["price"] = 0
        errors = validate_product(product_data)

        # Comprobar que hay un error de validación en el campo 'price'
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "El precio debe ser mayor que cero")
