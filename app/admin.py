from django.contrib import admin

from .models import Breed, Client, Pet, Vet

# Register your models here.
admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(Vet)
admin.site.register(Client)
