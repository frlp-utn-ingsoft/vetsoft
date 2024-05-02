from django.db import models


def validate_client(data):
    errors = {}

    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if phone == "":
        errors["phone"] = "Por favor ingrese un teléfono"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif email.count("@") == 0:
        errors["email"] = "Por favor ingrese un email valido"

    return errors


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def save_client(cls, client_data):
        errors = validate_client(client_data)

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
        self.name = client_data.get("name", "") or self.name
        self.email = client_data.get("email", "") or self.email
        self.phone = client_data.get("phone", "") or self.phone
        self.address = client_data.get("address", "") or self.address

        self.save()

def validate_medicines(data):
        errors = {}
        name = data.get("name", "")
        description = data.get("description", "")
        dose = data.get("dose", "")

        if name == "":
            errors["name"] = "Por favor, ingrese un nombre para la medicina"

        if description == "":
            errors["description"] = "Por favor, ingrese una descripcion"
        
        if dose == "":
            errors["dose"] = "Por favor, ingrese una dosis para la medicina"

        return errors



class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dose = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
    @classmethod
    def save_medicine(cls, medicine_data):
        errors = validate_medicines(medicine_data)

        if len(errors.keys()) > 0:
            return False, errors
            
        Medicine.objects.create(
            name=medicine_data.get("name"),
            description=medicine_data.get("description"),
            dose=medicine_data.get("dose"),
            )
        
        return True, None
    
    def update_medicine(self, medicine_data):
        self.name = medicine_data.get("name", "") or self.name
        self.description = medicine_data.get("description", "") or self.description
        self.dose = medicine_data.get("dose", "") or self.dose

        self.save()

def validate_vet(data):
        errors = {}
        name = data.get("name", "")
        email = data.get("email", "")
        phone = data.get("phone", "")

        if name == "":
            errors["name"] = "Por favor, ingrese el nombre del veterinario/a"

        if email == "":
            errors["email"] = "Por favor ingrese un email del veterinario/a"
        elif email.count("@") == 0:
            errors["email"] = "Por favor ingrese un email válido del veterinario/a"
        
        if phone == "":
            errors["phone"] = "Por favor, ingrese el telefono del veterinario/a"

        return errors

class Vet(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
        
    @classmethod
    def save_vet(cls, vet_data):
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors
            
        Vet.objects.create(
            name=vet_data.get("name"),
            email=vet_data.get("email"),
            phone=vet_data.get("phone"),
            )
        return True, None
    
    def update_vet(self, vet_data):
        self.name = vet_data.get("name", "") or self.name
        self.email = vet_data.get("email", "") or self.email
        self.phone = vet_data.get("phone", "") or self.phone

        self.save()