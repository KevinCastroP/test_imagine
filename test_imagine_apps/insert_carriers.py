import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_imagine_apps.settings')
django.setup()

from logistics.models import Transportista

def insertar_transportistas():
    # Crear instancias de Transportista
    transportistas = [
        Transportista(nombre='Juan Pérez', tipo_vehiculo='Camión', contacto='1234567890'),
        Transportista(nombre='María López', tipo_vehiculo='Furgoneta', contacto='9876543210'),
        Transportista(nombre='Pedro Gómez', tipo_vehiculo='Moto', contacto='4567891230'),
        Transportista(nombre='Laura Torres', tipo_vehiculo='Camión', contacto='3216549870'),
        Transportista(nombre='Carlos Ramírez', tipo_vehiculo='Furgoneta', contacto='7891234560'),
    ]

    # Guardar los transportistas en la base de datos
    for transportista in transportistas:
        transportista.save()

    print("Se han insertado los transportistas en la base de datos.")

if __name__ == "__main__":
    insertar_transportistas()
