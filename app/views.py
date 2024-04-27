from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Client
from .models import Medicine #Importa el modelo de Medicine

def home(request):
    return render(request, "home.html")


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
            request, "clients/form.html", {"errors": errors, "client": request.POST}
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


# Vista para mostrar todos los medicamentos en el repositorio
def medicines_repository(request):
    medicines = Medicine.objects.all()
    return render(request, "medicines/repository.html", {"medicines": medicines})

# Vista para el formulario de creación/edición de medicamentos
def medicines_form(request, id=None):
    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            # Guarda un nuevo medicamento
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            # Actualiza un medicamento existente
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            medicine.update_medicine(request.POST)

        if saved:
            # Redirige a la página del repositorio de medicamentos
            return redirect(reverse("medicines_repo"))

        # Renderiza el formulario con errores si no se pudo guardar
        return render(
            request, "medicines/form.html", {"errors": errors, "medicine": request.POST}
        )

    # Obtiene el medicamento si se está editando
    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)

    # Renderiza el formulario con los datos del medicamento
    return render(request, "medicines/form.html", {"medicine": medicine})

# Vista para eliminar un medicamento
def medicines_delete(request):
    medicine_id = request.POST.get("medicine_id")
    medicine = get_object_or_404(Medicine, pk=int(medicine_id))
    medicine.delete()

    # Redirige a la página del repositorio de medicamentos
    return redirect(reverse("medicines_repo"))
