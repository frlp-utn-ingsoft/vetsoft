
from django.db import models

#CLIENTES
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


class Product(models.Model):
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=25)
    price = models.FloatField()

    @classmethod
    def save_product(cls, product_data: dict) -> tuple[bool, dict | None]:
        errors = cls.validate_product(product_data)

        if errors:
            return False, errors

        Product.objects.create(
            name=product_data.get("name"),
            type=product_data.get("type"),
            price=product_data.get("price"),
        )
        return True, None

    @classmethod
    def validate_product(cls, data: dict) -> dict | None:
        """Return the dict of text for the fields with errors (if exists any) None otherwise"""
        errors = {
            "name": "Por favor ingrese un nombre",
            "type": "Por favor ingrese un tipo",
            "price": "Por favor ingrese un precio"
        }
        for key in list(errors.keys()):
            if data.get(key):
                errors.pop(key)
        return errors or None

    def update_product(self, product_data: dict)  -> tuple[bool, dict | None]:
        errors = self.validate_product(product_data)

        if errors:
            return False, errors

        self.name = product_data.get("name", self.name)
        self.type = product_data.get("type", self.type)
        self.price = product_data.get("price", self.price)
        self.save()
        return True, None

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    dose = models.IntegerField()

    @classmethod
    def save_medicine(cls, medicine_data: dict) -> tuple[bool, dict | None]:
        errors = cls.validate_medicine(medicine_data)

        if errors:
            return False, errors

        Medicine.objects.create(
            name=medicine_data.get("name"),
            description=medicine_data.get("description"),
            dose=medicine_data.get("dose"),
        )
        return True, None

    @classmethod
    def validate_medicine(cls, data: dict) -> dict | None:
        errors = {
            "name": "Por favor ingrese un nombre",
            "description": "Por favor ingrese una descripción",
            "dose": "Por favor ingrese una dosis",
        }
        for key in list(errors.keys()):
            if data.get(key):
                errors.pop(key)
        return errors or None

    def update_medicine(self, medicine_data: dict) -> tuple[bool, dict | None]:
        errors = self.validate_medicine(medicine_data)

        if errors:
            return False, errors

        self.name = medicine_data.get("name", self.name)
        self.description = medicine_data.get("description", self.description)
        self.dose = medicine_data.get("dose", self.dose)
        self.save()
        return True, None

    def __str__(self):
        return self.name


#VETS
def validate_vet(data):
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


class Vet(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

    @classmethod
    def save_vet(cls, vet_data):
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Vet.objects.create(
            name=vet_data.get("name"),
            phone=vet_data.get("phone"),
            email=vet_data.get("email"),
        )

        return True, None

    def update_vet(self, vet_data):
        self.name = vet_data.get("name", "") or self.name
        self.email = vet_data.get("email", "") or self.email
        self.phone = vet_data.get("phone", "") or self.phone

        self.save()


class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def save_provider(cls, provider_data):
        errors = validate_provider(provider_data)

        if len(errors.keys()) > 0:
            return False, errors

        Provider.objects.create(
            name=provider_data.get("name"),
            phone=provider_data.get("phone"),
            email=provider_data.get("email"),
            address=provider_data.get("address"),
        )

        return True, None

    def update_provider(self, provider_data):
        self.name = provider_data.get("name", "") or self.name
        self.email = provider_data.get("email", "") or self.email
        self.phone = provider_data.get("phone", "") or self.phone
        self.address = provider_data.get("address", "") or self.address

        self.save()

def validate_provider(data):
    errors = {}

    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    address = data.get("address", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if phone == "":
        errors["phone"] = "Por favor ingrese un teléfono"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif email.count("@") == 0:
        errors["email"] = "Por favor ingrese un email valido"

    if address == "":
        errors["address"] = "Por favor ingrese una dirección"

    return errors

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50, blank=True)
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
