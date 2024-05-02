from django.db import models

def validate_fields(data, required_fields):
    errors = {}

    for key, value in required_fields.items():
        field_value = data.get(key, "")
        if field_value == "":
            errors[key] = f"Por favor ingrese un {value}"
        elif key == 'email' and field_value.count("@") == 0:
            errors["email"] = "Por favor ingrese un email valido"

    return errors

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_required_fields():
        return {
            "name": "nombre",
            "email": "email",
            "phone": "teléfono"
        }

    @classmethod
    def save_client(cls, client_data):
        errors = validate_fields(client_data, Client.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        Client.objects.create(
            name=client_data.get("name"),
            phone=client_data.get("phone"),
            email=client_data.get("email"),
            address=client_data.get("address"),
        )

        return True, None

    def update_client(self, client_data):
        errors = validate_fields(client_data, Client.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        self.name = client_data.get("name", "") or self.name
        self.email = client_data.get("email", "") or self.email
        self.phone = client_data.get("phone", "") or self.phone
        self.address = client_data.get("address", "")

        self.save()

        return True, None

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_required_fields():
        return {
            "name": "nombre",
            "breed": "raza", 
            "birthday": "fecha de nacimiento"
        }

    @classmethod
    def save_pet(cls, pet_data):
        errors = validate_fields(pet_data, Pet.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
        )

        return True, None
    
    def update_pet(self, pet_data):
        errors = validate_fields(pet_data, Pet.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        self.name = pet_data.get("name", "") or self.name
        self.breed = pet_data.get("breed", "") or self.breed
        self.birthday = pet_data.get("birthday", "") or self.birthday

        self.save()

        return True, None

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    dose = models.IntField

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_required_fields():
        return {
            "name": "nombre",
            "description": "descripción", 
            "dose": "dosis"
        }

    @classmethod
    def save_medicine(cls, medicine_data):
        errors = validate_fields(medicine_data, Medicine.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        Medicine.objects.create(
            name=medicine_data.get("name"),
            description=medicine_data.get("description"),
            dose=medicine_data.get("dose"),
        )

        return True, None
    
    def update_medicine(self, medicine_data):
        errors = validate_fields(medicine_data, Medicine.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        self.name = medicine_data.get("name", "") or self.name
        self.description = medicine_data.get("breed", "") or self.breed
        self.dose = medicine_data.get("birthday", "") or self.birthday

        self.save()

        return True, None