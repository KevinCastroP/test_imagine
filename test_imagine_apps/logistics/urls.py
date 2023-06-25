from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.package_list, name='package_list'),
    path('packages/create_package/', views.create_package, name='create_package'),
    path('api/packages/<int:paquete_id>/assign/<int:transportista_id>/', views.PackageAssignView.as_view()),
    path('api/packages/<int:paquete_id>/update/', views.PackageUpdateView.as_view())
]
