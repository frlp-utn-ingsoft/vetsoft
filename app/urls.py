from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    path("medicines/", view=views.medicines_repository, name="medicines_repo"),
    path("medicines/nuevo/", view=views.medicines_form, name="medicines_form"),
    path("medicines/editar/<int:id>/", view=views.medicines_form, name="medicines_edit"),
    path("medicines/eliminar/", view=views.medicines_delete, name="medicines_delete"),
    path("veterinario/", view=views.vet_repository, name="vet_repo"),
    path("veterinario/nuevo/", view=views.vet_form, name="vet_form"),
    path("veterinario/editar/<int:id>/", view=views.vet_form, name="vet_edit"),
    path("veterinario/eliminar/", view=views.vet_delete, name="vet_delete"),
]