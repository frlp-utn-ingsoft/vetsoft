from django.test import TestCase
from app.models import Client, validate_product,validate_medicine, validate_pet, Pet, Breed


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

#test para ver si la clase enumerativa de raza existe
class TestBreedEnum(TestCase):
    def test_breed_enum_exists(self):
        # Verifica que la enumeración Breed existe
        self.assertTrue(hasattr(Breed, 'BEAGLE'))
        self.assertTrue(hasattr(Breed, 'LABRADOR'))
        self.assertTrue(hasattr(Breed, 'PUG'))
        self.assertTrue(hasattr(Breed, 'BULLDOG'))

        # Verifica los valores de la enumeración
        self.assertEqual(Breed.BEAGLE, "beagle")
        self.assertEqual(Breed.LABRADOR, "labrador")
        self.assertEqual(Breed.PUG, "pug")
        self.assertEqual(Breed.BULLDOG, "bulldog")

class PetModelTest(TestCase):
     
     #creacion de mascota con raza seleccionada
     def test_can_create_pet(self):
          # Crear una instancia de Mascota con una raza seleccionada
        mascota_data = {
            "name": "Charly",
            "breed": "Pug",
            "birthday": "2020-06-18",
            "weight": 130
        }
        errors = validate_pet(mascota_data)
        # verifica que no hay error en el peso
        self.assertNotIn("breed", errors, "No debe haber un error de seleccion de raza")

    #creacion de mascota sin raza seleccionada
     def test_cant_create_pet(self):
          # Crear una instancia de Mascota SIN una raza seleccionada
        mascota_data = {
            "name": "Charly",
            "breed": "",
            "birthday": "2020-06-18",
            "weight": 130
        }
        errors = validate_pet(mascota_data)
        # verifica que salga el error correspondiente
        self.assertEqual(errors["breed"], "Por favor seleccione una raza")
         # Verificar que no se haya creado la mascota en la base de datos
        self.assertEqual(Pet.objects.count(), 0)



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
