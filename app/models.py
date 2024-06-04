from django.db import models


def validate_client(data):
    """ Valida los datos del cliente """
    errors = {}

    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"
    elif not re.match("^[a-zA-Z ]+$", name):
        errors["name"] = "El nombre solo puede contener letras y espacios"

    if phone == "":
        errors["phone"] = "Por favor ingrese un teléfono"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif email.count("@") == 0:
        errors["email"] = "Por favor ingrese un email valido"

    return errors


def validate_provider(data):
    """ Valida los datos del proveedor """
    errors = {}

    name = data.get("name", "")
    email = data.get("email", "")
    address = data.get("address", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre"

    if email == "":
        errors["email"] = "Por favor ingrese un email"
    elif email.count("@") == 0:
        errors["email"] = "Por favor ingrese un email válido"

    if address == "":
        errors["address"] = "Por favor ingrese una dirección"

    return errors


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """Retorna la representación en cadena del cliente"""
        return self.name

    @classmethod
    def save_client(cls, client_data):
        """Guarda un nuevo cliente"""
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
        """Actualiza un cliente existente"""
        errors = validate_client(client_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = client_data.get("name", "") or self.name
        self.email = client_data.get("email", "") or self.email
        self.phone = client_data.get("phone", "") or self.phone
        self.address = client_data.get("address", "") or self.address

        self.save()

        return True, None



class Breed(models.TextChoices):
    DOG = "Dog",
    CAT = "Cat",
    BIRD = "Bird"

def validate_pet(data):
    """Valida los datos de la mascosta"""
    errors = {}

    name = data.get("name", "")
    breed = data.get("breed", "")
    birthday = data.get("birthday", "")

    if name == "":
        errors["name"] = "Por favor ingrese un nombre de la mascota"

    if breed == "":
        errors["breed"] = "Por favor ingrese la raza de la mascota"

    if birthday == "":
        errors["birthday"] = "Por favor ingrese la fecha de nacimiento de la mascota"

    return errors


class Pet(models.Model):

    name = models.CharField(max_length=100)
    breed = models.CharField(
        max_length=100,
        choices=Breed.choices,
        default=Breed.DOG,
    )
    birthday = models.DateField()

    def __str__(self):
        """Retorna la representación en cadena de la mascota"""
        return self.name

    @classmethod
    def save_pet(cls, pet_data):
        """Guarda una nueva mascota"""
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday")

        )
        return True, None

    def update_pet(self, pet_data):
        """Actualiza una mascota existente"""
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = pet_data.get("name", None) or self.name
        self.breed = pet_data.get("breed", None) or self.breed
        self.birthday = pet_data.get("birthday", None) or self.birthday

        self.save()


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        """Retorna la representación en cadena del proveedor"""
        return self.name

    @classmethod
    def save_provider(cls, provider_data):
        """Guarda un nuevo proveedor"""

        errors = validate_provider(provider_data)
        if len(errors.keys()) > 0:
            return False, errors

        Provider.objects.create(
            name=provider_data.get("name"),
            email=provider_data.get("email"),
            address=provider_data.get("address"),
        )

        return True, None

    def update_provider(self, provider_data):
        """Actualiza un proveedor existente"""

        errors = validate_provider(provider_data)
        if len(errors.keys()) > 0:
            return False, errors
        
        self.name = provider_data.get("name", "") or self.name
        self.email = provider_data.get("email", "") or self.email
        self.address = provider_data.get("address", "") or self.address

        self.save()


def isfloat(num):
    """Verifica si el valor dado es un número flotante"""
    try:
        float(num)
        return True
    except ValueError:
        return False


def validate_product(data):
    """Valida los datos del producto"""
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
    elif not isfloat(price):
        errors["price"] = "Por favor ingrese un precio"
    elif float(price) <= 0:
        errors["price"] = "El precio debe ser mayor a cero"

    return errors


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        """Retorna la representación en cadena del producto"""
        return self.name

    @classmethod
    def save_product(cls, product_data):
        """Guarda un nuevo producto"""
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
        """Acutaliza un producto existente"""
        errors = validate_product(product_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = product_data.get("name", "") or self.name
        self.type = product_data.get("type", "") or self.type
        self.price = product_data.get("price", "") or self.price

        self.save()

        return True, None

# class Speciality(models.TextChoices):
#     GENERAL = 'General', 'General'
#     SURGEON = 'Surgeon', 'Surgeon'
#     DENTIST = 'Dentist', 'Dentist'
#     CARDIOLOGIST = 'Cardiologist', 'Cardiologist'

def validate_vet(data):
    """Valida los datos del veterinario"""
    errors = {}

    name = data.get("name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    speciality = data.get("especialidad", "")

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

    if speciality == "":
        errors["especialidad"] = "Por favor seleccione una especialidad"
    # elif speciality not in [choice[0] for choice in Speciality.choices]:
    #     errors["speciality"] = "Especialidad no válida"

    return errors


class Vet(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)
    speciality = models.CharField(max_length=15)

    def __str__(self):
        """Retorna la representación en cadena del veterinario"""
        return self.name

    @classmethod
    def save_vet(cls, vet_data):
        """Guarda un nuevo veterinario"""
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Vet.objects.create(
            name=vet_data.get("name"),
            phone=vet_data.get("phone"),
            email=vet_data.get("email"),
            address=vet_data.get("address"),
            speciality=vet_data.get("especialidad"),

        )

        return True, None

    def update_vet(self, vet_data):
        """Actualiza los datos de un veterinario existente"""
        errors = validate_vet(vet_data)

        if len(errors.keys()) > 0:
            return False, errors

        self.name = vet_data.get("name", "") or self.name
        self.email = vet_data.get("email", "") or self.email
        self.phone = vet_data.get("phone", "") or self.phone
        self.address = vet_data.get("address", "") or self.address
        self.speciality = vet_data.get("especialidad", "") or self.speciality
        
        self.save()

        return True, None

# Función de validación de medicamentos


def validate_medicine(data):
    """Valida los datos del medicamento"""
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
        errors["dose"] = "La dosis debe ser un número entero positivo"
    else:
        dose_value = int(dose)
        if dose_value < 1 or dose_value > 10:
            errors["dose"] = "La dosis debe estar entre 1 a 10"

    return errors

# Definition of the Medicine model


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dose = models.IntegerField()

    def __str__(self):
        """Retorna la representación en cadena del medicamento"""
        return self.name

# Método de clase para guardar un nuevo medicamento
    @classmethod
    def save_medicine(cls, medicine_data):
        """Guarda un nuevo medicamento"""
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
        """Actualiza un medicamento existente"""
        errors = validate_medicine(medicine_data)
        if len(errors.keys()) > 0:
            return False, errors
    
        self.name = medicine_data.get("name", "") or self.name
        self.description = medicine_data.get("description", "") or self.description
        self.dose = medicine_data.get("dose", "") or self.dose

        self.save()
        
        return True, None
