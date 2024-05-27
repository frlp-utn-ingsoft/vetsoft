from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Client, Pet, Breed
from django.http import HttpResponseBadRequest
from datetime import datetime


def home(request):
    return render(request, "home.html")

########################### SEPARADOR ###################################
# views de clientes
#########################################################################


def clients_repository(request):
    clients = Client.objects.all()
    return render(request, "clients/repository.html", {"clients": clients})


def clients_form(request, id=None):
    if request.method == "POST":
        client_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if client_id == "":
            saved, errors = Client.save_client(request.POST)
        else:
            client = get_object_or_404(Client, pk=client_id)
            client.update_client(request.POST)

        if saved:
            return redirect(reverse("clients_repo"))

        return render(
            request, "clients/form.html", {"errors": errors,
                                           "client": request.POST}
        )

    client = None
    if id is not None:
        client = get_object_or_404(Client, pk=id)

    return render(request, "clients/form.html", {"client": client})


def clients_delete(request):
    client_id = request.POST.get("client_id")
    client = get_object_or_404(Client, pk=int(client_id))
    client.delete()

    return redirect(reverse("clients_repo"))

########################### SEPARADOR ###################################
# creo las vistas para la lista de mascotas
#########################################################################


def pets_repository(request):
    pets = Pet.objects.all()
    return render(request, "pets/repository.html", {"pets": pets})


# def pets_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         breed = request.POST.get('breed')
#         birthday = request.POST.get('birthday')
#         owner_id = request.POST.get('owner')
#         owner = Client.objects.get(id=owner_id)

#         Pet.objects.create(name=name, breed=breed,
#                            birthday=birthday, owner=owner)

#         # Asume que tienes una vista llamada 'pets_list'
#         return redirect('pets_repo')
#     else:
#         clients = Client.objects.all()
#         return render(request, 'pets/form.html', {'clients': clients})

def pets_form(request, id=None):

    breeds = Breed.choices

    if id:
        pet = get_object_or_404(Pet, id=id)
    else:
        pet = None

    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        birthday = request.POST.get('birthday')
        owner_id = request.POST.get('owner')
        owner = Client.objects.get(id=owner_id)

        pet_data = {
            'name': name,
            'breed': breed,
            'birthday': birthday,
            'owner': owner,
        }

        if pet:
            pet.update_pet(pet_data)
        else:
            Pet.save_pet(pet_data, owner)

        # Asume que tienes una vista llamada 'pets_list'
        return redirect('pets_repo')
    else:
        clients = Client.objects.all()
        return render(request, 'pets/form.html', {'clients': clients, 'pet': pet, "breeds": breeds})


def pets_delete(request):
    pet_id = request.POST.get("pet_id")
    pet = get_object_or_404(Pet, pk=int(pet_id))
    pet.delete()

    return redirect(reverse("pets_repo"))
