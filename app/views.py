from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Client, Provider, Medicine, Product
from django.http import HttpResponseBadRequest



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

def providers_repository(request):
    providers = Provider.objects.all()
    return render(request, "providers/repository.html", {"providers": providers})

def providers_form(request, id=None):
    if request.method == "POST":
        provider_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if provider_id == "":
            saved, errors = Provider.save_provider(request.POST)
        else:
            provider = get_object_or_404(Provider, pk=provider_id)
            provider.update_provider(request.POST)

        if saved:
            return redirect(reverse("providers_repo"))

        return render(
            request, "providers/form.html", {"errors": errors, "provider": request.POST}
        )

    provider = None
    if id is not None:
        provider = get_object_or_404(Provider, pk=id)

    return render(request, "providers/form.html", {"provider": provider})

def providers_delete(request):
    provider_id = request.POST.get("provider_id")
    provider = get_object_or_404(Provider, pk=int(provider_id))
    provider.delete()

    return redirect(reverse("providers_repo"))

def medicine_form(request, id=None):
    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            medicine.update_medicine(request.POST)

        if saved:
            return redirect(reverse("medicine_repo"))

        return render(
            request, "medicine/form.html", {"errors": errors, "medicine": request.POST}
        )

    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)
    
        if not hasattr(medicine, 'name'):
            medicine.name = ''

    return render(request, "medicine/form.html", {"medicine": medicine})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine/list.html', {'medicines': medicines})

def medicine_delete(request):
    if request.method == "POST":
        medicine_id = request.POST.get("medicine_id")
        if medicine_id:
            medicine = get_object_or_404(Medicine, pk=int(medicine_id))
            medicine.delete()
            return redirect(reverse("medicine_repo"))
    # Si la solicitud no es POST o no se proporciona un ID de medicina válido,devolvemos un error de solicitud incorrecta.
    return HttpResponseBadRequest("Solicitud incorrecta")
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
