from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Client, Vet, Medi


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


def vets_repository(request):
    vets = Vet.objects.all()
    return render(request, "vets/repository.html", {"vets": vets})


def vets_form(request, id=None):
    if request.method == "POST":
        vet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if vet_id == "":
            saved, errors = Vet.save_vet(request.POST)
        else:
            vet = get_object_or_404(Vet, pk=vet_id)
            vet.update_vet(request.POST)

        if saved:
            return redirect(reverse("vets_repo"))

        return render(
            request, "vets/form.html", {"errors": errors, "vet": request.POST}
        )

    vet = None
    if id is not None:
        vet = get_object_or_404(Vet, pk=id)

    return render(request, "vets/form.html", {"vet": vet})

def vets_delete(request):
    vet_id = request.POST.get("vet_id")
    vet = get_object_or_404(Vet, pk=int(vet_id))
    vet.delete()

    return redirect(reverse("vets_repo"))


#medicine
def medis_repository(request):
    medis = Medi.objects.all()
    return render(request, "medicine/repository.html", {"medis": medis})


def medis_form(request, id=None):
    if request.method == "POST":
        medi_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medi_id == "":
            saved, errors = Vet.save_medi(request.POST)
        else:
            medi = get_object_or_404(Medi, pk=medi_id)
            medi.update_medi(request.POST)

        if saved:
            return redirect(reverse("medi_repo"))

        return render(
            request, "medis/form.html", {"errors": errors, "medi": request.POST}
        )

    medi = None
    if id is not None:
        medi = get_object_or_404(medi, pk=id)

    return render(request, "medis/form.html", {"medi": medi})

def medis_delete(request):
    medi_id = request.POST.get("medi_id")
    medi = get_object_or_404(medi, pk=int(medi_id))
    medi.delete()

    return redirect(reverse("medis_repo"))