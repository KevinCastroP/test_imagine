from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.package_list, name='package_list'),
]
