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


class pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50, blank=True)
    birthday = models.DateField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='pets') ##conexion con cliente (su propietario)

    def __str__(self):
        return self.name
    
    @classmethod
    def save_pet(cls, pet_data):
        owner_id = pet_data.pop("owner_id", None)  # Obtenemos el ID del propietario

        if owner_id is None:
            raise ValueError("El ID del propietario es necesario para guardar la mascota.")
        
        owner = Client.objects.get(pk=owner_id)  # Obtenemos el propietario desde la base de datos

         # Creamos la mascota y la asociamos al propietario
        pet = cls.objects.create(
            owner=owner,
            name=pet_data.get("name"),
            breed=pet_data.get("breed"),
            birthday=pet_data.get("birthday"),
            )

        return pet
    
    def update_pet(cls, pet_data):
        pet.name = pet_data.get("name", pet.name)
        pet.breed = pet_data.get("breed", pet.breed)
        pet.birthday = pet_data.get("birthday", pet.birthday)
        pet.save()

        


    
    
