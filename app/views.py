from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .models import Client, Medicine, Product, Vet, Provider

def home(request):
    return render(request, "home.html")

#CLIENTS
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

############################################# PRODUCTS #############################################
class ProductRepositoryView(TemplateView):
    template_name = "products/repository.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


class ProductFormView(View):
    template_name = "products/form.html"

    def get(self, request, id=None):
        context = {}
        if id is not None:
            context["product"] = get_object_or_404(Product, pk=id)
        return render(request, self.template_name, context)

    def post(self, request, id=None):
        product_id = request.POST.get("id", "")
        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            saved, errors = product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))
        return render(request, self.template_name, {"errors": errors, "product": request.POST})

class ProductDeleteView(View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, pk=int(product_id))
        product.delete()
        return redirect(reverse("products_repo"))
####################################################################################################

############################################ MEDICINAS #############################################

class MedicineRepositoryView(TemplateView):
    template_name = "medicines/repository.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medicines"] = Medicine.objects.all()
        return context

class MedicineFormView(View):
    template_name = "medicines/form.html"

    def get(self, request, id=None):
        context = {}
        if id is not None:
            context["medicine"] = get_object_or_404(Medicine, pk=id)
        return render(request, self.template_name, context)

    def post(self, request, id=None):
        medicine_id = request.POST.get("id", "")
        if medicine_id == "":
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            saved, errors = medicine.update_medicine(request.POST)

        if saved:
            return redirect(reverse("medicines_repo"))
        return render(request, self.template_name, {"errors": errors, "medicine": request.POST})

class MedicineDeleteView(View):
    def post(self, request):
        medicine_id = request.POST.get("medicine_id")
        medicine = get_object_or_404(Medicine, pk=int(medicine_id))
        medicine.delete()
        return redirect(reverse("medicines_repo"))
####################################################################################################

############################################# VETS #############################################
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
####################################################################################################
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
