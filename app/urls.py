from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    
    path("vets/", view=views.vets_repository, name="vets_repo"),
    path("vets/nuevo/", view=views.vets_form, name="vets_form"),
    path("vets/editar/<int:id>/", view=views.vets_form, name="vets_edit"),
    path("vets/eliminar/", view=views.vets_delete, name="vets_delete"),
    
    path("medicine/", view=views.medicine_repository, name="medicine_repo"),
    path("medicine/nuevo/", view=views.medicine_form, name="medicine_form"),
    path("medicine/editar/<int:id>/", view=views.medicine_form, name="medicine_edit"),
    path("medicine/eliminar/", view=views.medicine_delete, name="medicine_delete"),

    path("mascotas/", view=views.pets_repository, name="pets_repo"),
    path("mascotas/nuevo/", view=views.pets_form, name="pets_form"),
    path("mascota/editar/<int:id>/", view=views.pets_form, name="pets_edit"),
    path("mascota/eliminar", view=views.pets_delete, name="pets_delete"),
]
