from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.package_list, name='package_list'),
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/<int:cliente_id>/paquetes_enviados/', views.package_send_by_client, name='paquetes_enviados'),
    path('carrier/<int:transportista_id>/paquetes_asignados/', views.carrier_assigned_packages, name='paquetes_asignados'),
    path('packages/create/', views.create_package, name='create_package'),
    path('packages/edit/<int:paquete_id>/', views.edit_package, name='editar_paquete'),
    path('packages/delete/<int:paquete_id>/', views.delete_package, name='eliminar_paquete')
]
