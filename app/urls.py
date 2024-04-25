from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    path("proveedores/", view=views.providers_repository, name="providers_repo"),
    path("proveedores/nuevo/", view=views.providers_form, name="providers_form"),
    path("proveedores/editar/<int:id>/", view=views.providers_form, name="providers_edit"),
    path("proveedores/eliminar/", view=views.providers_delete, name="providers_delete"),
    path("medicine/new/", views.medicine_form, name="medicine_form"),
    path("medicine/", views.medicine_form, name="medicine_repo"),
    path("medicine/editar/<int:id>/", view=views.medicine_form, name="medicine_edit"),
    path('medicine/list/', views.medicine_list, name='medicine_list'),
    path("medicine/delete/", view=views.medicine_delete, name="medicine_delete"),
    path("productos/", view=views.products_repository, name="products_repo"),
    path("productos/nuevo", view=views.products_form, name="products_form"),
    path("productos/editar/<int:id>/", view=views.products_form, name="products_edit"),
    path("productos/eliminar/", view=views.products_delete, name="products_delete"),
]
