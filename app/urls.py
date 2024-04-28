from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    
    path("medicine/", view=views.medicine_repository, name="medicine_repo"),
    path("medicine/nuevo/", view=views.medicine_form, name="medicine_form"),
    path("medicine/editar/<int:id>/", view=views.medicine_form, name="medicine_edit"),
    path("medicine/eliminar/", view=views.medicine_delete, name="medicine_delete"),
]
