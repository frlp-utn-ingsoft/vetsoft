# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(Vet)
admin.site.register(Client)
