from django.urls import reverse

# agregamos un nuevo contexto para el navbar de mascotas
links = [
    {"label": "Home", "href": reverse("home"), "icon": "bi bi-house-door"},
    {"label": "Clientes", "href": reverse(
        "clients_repo"), "icon": "bi bi-people"},
    {"label": "Mascotas", "href": reverse("pets_repo"), "icon": "bi bi-paw"}]


def navbar(request):
    def add_active(link):
        copy = link.copy()

        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))

        return copy

    return {"links": map(add_active, links)}
