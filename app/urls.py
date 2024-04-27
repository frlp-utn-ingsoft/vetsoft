from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),

    #URLS del modelo Vet
    path("veterinaria/", view=views.vets_repository, name="vets_repo"),
    path("veterinaria/nuevo/", view=views.vets_form, name="vets_form"),
    path("veterinaria/editar/<int:id>/", view=views.vets_form, name="vets_edit"),
    path("veterinaria/eliminar/", view=views.vets_delete, name="vets_delete"),
]
