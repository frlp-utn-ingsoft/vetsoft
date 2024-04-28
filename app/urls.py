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
    path("medicinas/", view=views.meds_repository, name="meds_repo"),
    path("medicinas/nuevo/", view=views.meds_form, name="meds_form"),
    path("medicinas/editar/<int:id>/", view=views.meds_form, name="meds_edit"),
    path("medicinas/eliminar/", view=views.meds_delete, name="meds_delete"),
]
