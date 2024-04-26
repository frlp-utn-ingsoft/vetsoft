from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),

    path("medicamentos/", view=views.medicines_repository, name="medicines_repo"),
    path("medicamentos/nuevo/", view=views.medicines_form, name="medicines_form"),
    path("medicamentos/editar/<int:id>/", view=views.medicines_form, name="medicines_edit"),
    path("medicamentos/eliminar/", view=views.medicines_delete, name="medicines_delete"),

    ##pet
    path("mascotas/nuevo/", view=views.pets_form, name="pets_form"),
]
