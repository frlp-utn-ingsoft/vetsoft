from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),

    path("productos/", views.ProductRepositoryView.as_view(), name="products_repo"),
    path("productos/nuevo/", views.ProductFormView.as_view(), name="products_create"),
    path("productos/editar/<int:id>/", views.ProductFormView.as_view(), name="products_edit"),
    path("productos/eliminar/", views.ProductDeleteView.as_view(), name="products_delete"),

]
