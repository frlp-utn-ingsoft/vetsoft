from django.urls import reverse

links = [
    {"label": "Home", "href": reverse("home"), "icon": "bi bi-house-door"},
    {"label": "Clientes", "href": reverse("clients_repo"), "icon": "bi bi-people"},
    {"label": "Proveedores", "href": reverse("providers_repo"), "icon": "bi bi-people"},
    {"label": "Productos", "href": reverse("products_repo"), "icon": "bi bi-basket3"},
    {"label": "Medicinas", "href": reverse("medicine_repo"), "icon": "bi bi-capsule"}
]


def navbar(request):
    def add_active(link):
        copy = link.copy()

        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))

        return copy

    return {"links": map(add_active, links)}
