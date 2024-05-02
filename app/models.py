from django.db import models
from datetime import datetime


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

def validate_pet(data):
    errors = {}

    name = data.get("name", "")
    breed = data.get("breed", "")
    birthday = data.get("birthday", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if breed == "":
        errors["breed"] = "Por favor ingrese la raza"

    if birthday == "":
        errors["birthday"] = "Por favor ingrese una fecha"
    elif datetime.strptime(birthday, "%Y-%m-%d").date() > datetime.now().date():
        errors["birthday"] = "La fecha de cumpleaños no puede ser mayor al dia actual"

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
    
def validate_products(data):
        errors = {}
        name = data.get("name", "")
        type = data.get("type", "")
        price = data.get("price", "")

        if name == "":
            errors["name"] = "Ingrese el nombre del producto"

        if type == "":
            errors["type"] = "Ingrese el tipo de producto"
        
        if price == "":
            errors["price"] = "Ingrese precio del producto, el precio no puede ser 0"

        return errors

class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.FloatField()

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
    def save_product(cls, product_data):
        errors = validate_products(product_data)
    def save_vet(cls, vet_data):
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors
            
        Product.objects.create(
            name=product_data.get("name"),
            type=product_data.get("type"),
            price=product_data.get("price"),
            )
        
        return True, None
    
    def update_product(self, product_data):
        self.name = product_data.get("name", "") or self.name
        self.type = product_data.get("type", "") or self.type
        self.price = product_data.get("price", "") or self.price

        self.save()
        
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=300)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
    @classmethod
    def save_pet(cls, pet_data):
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
        )

        return True, None

    def update_pet(self, pet_data):
        self.name = pet_data.get("name", "") or self.name
        self.breed = pet_data.get("breed", "") or self.breed
        self.birthday = pet_data.get("birthday", "") or self.birthday

        self.save()
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
