from django.urls import reverse

links = [
    {"label": "Home", "href": reverse("home"), "icon": "bi bi-house-door"},
    {"label": "Clientes", "href": reverse("clients_repo"), "icon": "bi bi-people"},
    {"label": "Animales", "href": reverse("pets_repo"), "icon": "fas fa-dog"},
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

def home_items(request):
    items = [
        {"label": "Clientes", "href": reverse("clients_repo"), "icon": "bi bi-people"},
        {"label": "Animales", "href": reverse("pets_repo"), "icon": "fas fa-dog"},
    ]
    return {"home_items": items}
