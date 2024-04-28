from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Client, Product , Med


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


def products_repository(request):
    products = Product.objects.all()
    return render(request, "products/repository.html", {"products": products})


def products_form(request, id=None):
    if request.method == "POST":
        product_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))

        return render(
            request, "products/form.html", {"errors": errors, "product": request.POST}
        )

    product = None
    if id is not None:
        product = get_object_or_404(Product, pk=id)

    return render(request, "products/form.html", {"product": product})


def products_delete(request):
    product_id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=int(product_id))
    product.delete()

    return redirect(reverse("products_repo"))


def meds_repository(request):
    meds = Med.objects.all()
    return render(request, "meds/repository.html", {"meds": meds})

def meds_form(request, id=None):
    if request.method == "POST":
        med_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if med_id == "":
            saved, errors = Med.save_med(request.POST)
        else:
            med = get_object_or_404(Med, pk=med_id)
            med.update_med(request.POST)

        if saved:
            return redirect(reverse("meds_repo"))

        return render(
            request, "meds/form.html", {"errors": errors, "med": request.POST}
        )

    med = None
    if id is not None:
        med = get_object_or_404(Med, pk=id)

    return render(request, "meds/form.html", {"med": med})

def meds_delete(request):
    med_id = request.POST.get("med_id")
    med = get_object_or_404(Med, pk=int(med_id))
    med.delete()

    return redirect(reverse("meds_repo"))
