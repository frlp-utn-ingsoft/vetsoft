from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from .models import Client, Product

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
