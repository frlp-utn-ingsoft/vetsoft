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
    def save_pet(cls, pet_data):
        errors = validate_pet(pet_data)

        if len(errors.keys()) > 0:
            return False, errors

        Pet.objects.create(
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
            owner=pet_data.get("owner"),
        )

        return True, None

    def update_pet(self, pet_data):
        self.name = pet_data.get("name", "") or self.name
        self.breed = pet_data.get("breed", "") or self.breed
        self.birthday = pet_data.get("birthday", "") or self.birthday
        self.owner = pet_data.get("owner", "") or self.owner

        self.save()
