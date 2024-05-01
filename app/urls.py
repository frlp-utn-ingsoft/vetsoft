from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    path("productos/", view=views.products_repository, name="products_repo"),
    path("productos/nuevo/", view=views.products_form, name="products_form"),
    path("productos/editar/<int:id>/", view=views.products_form, name="products_edit"),
    path("productos/eliminar/", view=views.products_delete, name="products_delete"),

    #URLS del modelo Vet
    path("veterinario/", view=views.vets_repository, name="vets_repo"),
    path("veterinario/nuevo/", view=views.vets_form, name="vets_form"),
    path("veterinario/editar/<int:id>/", view=views.vets_form, name="vets_edit"),
    path("veterinario/eliminar/", view=views.vets_delete, name="vets_delete"),
]
