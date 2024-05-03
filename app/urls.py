from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    path("productos/", view=views.products_repository, name="products_repo"),
    path("productos/nuevo/", view=views.product_form, name="products_form"),
    path("productos/editar/<int:id>/", view=views.product_form, name="products_edit"),
    path("productos/eliminar/", view=views.products_delete, name="products_delete"),
    
    path("medicine/", view=views.medicine_repository, name="medicine_repo"),
    path("medicine/nuevo/", view=views.medicine_form, name="medicine_form"),
    path("medicine/editar/<int:id>/", view=views.medicine_form, name="medicine_edit"),
    path("medicine/eliminar/", view=views.medicine_delete, name="medicine_delete"),

    path("mascotas/", view=views.pets_repository, name="pets_repo"),
    path("mascotas/nuevo/", view=views.pets_form, name="pets_form"),
    path("mascotas/editar/<int:id>/", view=views.pets_form, name="pets_edit"),
    path("mascotas/eliminar", view=views.pets_delete, name="pets_delete"),
    path("mascotas/agregar-medicina/<int:id>/", view=views.pets_add_medicine, name="pets_add_medicine"),
]
