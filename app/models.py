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


def validate_provider(data):
    errors = {}

    name = data.get("name", "")
    email = data.get("email", "")
    phone = data.get("phone", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if phone == "":
        errors["phone"] = "Por favor ingrese un teléfono"
    elif not phone.isdigit():
        errors["phone"] = "Por favor ingrese un teléfono"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif email.count("@") == 0:
        errors["email"] = "Por favor ingrese un email válido"

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
        errors = validate_client(client_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = client_data.get("name", "") or self.name
        self.email = client_data.get("email", "") or self.email
        self.phone = client_data.get("phone", "") or self.phone
        self.address = client_data.get("address", "") or self.address

        self.save()

        return True, None

########################### SEPARADOR ###################################
# agrego validacion de datos de mascota
#########################################################################


def validate_pet(data):
    errors = {}

    name = data.get("name", "")
    breed = data.get("breed", "")
    birthday = data.get("birthday", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre de la mascota"

    if breed == "":
        errors["phone"] = "Por favor ingrese la raza de la mascota"

    if birthday == "":
        errors["birthday"] = "Por favor ingrese la fecha de nacimiento de la mascota"

    return errors

########################### SEPARADOR ###################################
# creo modelo del pet
#########################################################################


class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)  # raza
    birthday = models.DateField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def save_pet(cls, pet_data, owner):
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
            owner=owner,

        )

        return True, None

    # def update_pet(self, pet_data):
    #     self.name = pet_data.get("name", "") or self.name
    #     self.breed = pet_data.get("breed", "") or self.breed
    #     self.birthday = pet_data.get("birthday", "") or self.birthday
    #     self.owner = pet_data.get("owner", "") or self.owner

    #     self.save()


def update_pet(self, pet_data):
    self.name = pet_data.get("name", None) or self.name
    self.breed = pet_data.get("breed", None) or self.breed
    self.birthday = pet_data.get("birthday", None) or self.birthday
    self.owner = pet_data.get("owner", None) or self.owner

    self.save()

########################### SEPARADOR ###################################
# agrego validacion de datos de mascota
#########################################################################


def validate_pet(data):
    errors = {}

    name = data.get("name", "")
    breed = data.get("breed", "")
    birthday = data.get("birthday", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre de la mascota"

    if breed == "":
        errors["phone"] = "Por favor ingrese la raza de la mascota"

    if birthday == "":
        errors["birthday"] = "Por favor ingrese la fecha de nacimiento de la mascota"

    return errors

########################### SEPARADOR ###################################
# creo modelo del pet
#########################################################################


class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)  # raza
    birthday = models.DateField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def save_pet(cls, pet_data, owner):
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
            owner=owner,

        )

        return True, None

    # def update_pet(self, pet_data):
    #     self.name = pet_data.get("name", "") or self.name
    #     self.breed = pet_data.get("breed", "") or self.breed
    #     self.birthday = pet_data.get("birthday", "") or self.birthday
    #     self.owner = pet_data.get("owner", "") or self.owner

    #     self.save()


def update_pet(self, pet_data):
    self.name = pet_data.get("name", None) or self.name
    self.breed = pet_data.get("breed", None) or self.breed
    self.birthday = pet_data.get("birthday", None) or self.birthday
    self.owner = pet_data.get("owner", None) or self.owner

    self.save()


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    @classmethod
    def save_provider(cls, provider_data):
        errors = validate_provider(provider_data)

        if len(errors.keys()) > 0:
            return False, errors

        Provider.objects.create(
            name=provider_data.get("name"),
            email=provider_data.get("email"),
        )

        return True, None

    def update_provider(self, provider_data):
        self.name = provider_data.get("name", "") or self.name
        self.email = provider_data.get("email", "") or self.email

        self.save()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def validate_product(data):
    errors = {}

    name = data.get("name", "")
    type = data.get("type", "")
    price = data.get("price", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if type == "":
        errors["type"] = "Por favor ingrese un tipo del producto"

    if price == "":
        errors["price"] = "Por favor ingrese un precio"
    elif isfloat(price) == False:
        errors["price"] = "Por favor ingrese un precio"
    elif float(price) <= 0:
        errors["price"] = "Por favor ingrese un precio"

    return errors


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @classmethod
    def save_product(cls, product_data):
        errors = validate_product(product_data)

        if len(errors.keys()) > 0:
            return False, errors

        Product.objects.create(
            name=product_data.get("name"),
            type=product_data.get("type"),
            price=product_data.get("price"),
        )

        return True, None

    def update_product(self, product_data):
        errors = validate_product(product_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = product_data.get("name", "") or self.name
        self.type = product_data.get("type", "") or self.type
        self.price = product_data.get("price", "") or self.price

        self.save()

        return True, None

def validate_vet(data):
    errors = {}

    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    opening_time = data.get("opening_time", "")
    closing_time = data.get("closing_time", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if phone == "":
        errors["phone"] = "Por favor ingrese un teléfono"
    elif not phone.isdigit():
        errors["phone"] = "Por favor ingrese un teléfono"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif "@" not in email:  # Agreo una verificacion para saber si hay al menos un "@" en el email
        errors["email"] = "Por favor ingrese un email válido"

    return errors


class Vet(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

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
            address=vet_data.get("address"),

        )

        return True, None

    def update_vet(self, vet_data):
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = vet_data.get("name", "") or self.name
        self.email = vet_data.get("email", "") or self.email
        self.phone = vet_data.get("phone", "") or self.phone
        self.address = vet_data.get("address", "") or self.address

        self.save()

        return True, None

# Función de validación de medicamentos


def validate_medicine(data):
    errors = {}

    name = data.get("name", "")
    description = data.get("description", "")
    dose = data.get("dose", "")

    # Validación del nombre
    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    # Validación de la descripción
    if description == "":
        errors["description"] = "Por favor ingrese una descripción"

    # Validación de la dosis
    if dose == "":
        errors["dose"] = "Por favor ingrese una dosis"
    elif not dose.isdigit():
        errors["dose"] = "La dosis debe ser un número entero"

    return errors

# Definition of the Medicine model


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dose = models.IntegerField()

    def __str__(self):
        return self.name

# Método de clase para guardar un nuevo medicamento
    @classmethod
    def save_medicine(cls, medicine_data):
        errors = validate_medicine(medicine_data)

        if len(errors.keys()) > 0:
            return False, errors

        Medicine.objects.create(
            name=medicine_data.get("name"),
            description=medicine_data.get("description"),
            dose=medicine_data.get("dose"),
        )

        return True, None

    # Método para actualizar un medicamento existente
    def update_medicine(self, medicine_data):
        errors = validate_medicine(medicine_data)
        if len(errors.keys()) > 0:
            return False, errors
    
        self.name = medicine_data.get("name", "") or self.name
        self.description = medicine_data.get("description", "") or self.description
        self.dose = medicine_data.get("dose", "") or self.dose

        self.save()
        
        return True, None
