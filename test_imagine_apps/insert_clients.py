import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_imagine_apps.settings')
django.setup()

from logistics.models import Cliente

def insertar_clientes():
    # Crear instancias de Cliente
    clientes = [
        Cliente(nombre='John Doe', direccion='123 Main St', telefono='1234567890'),
        Cliente(nombre='Jane Smith', direccion='456 Elm St', telefono='9876543210'),
        Cliente(nombre='Mike Johnson', direccion='789 Oak St', telefono='4567891230'),
        Cliente(nombre='Emily Davis', direccion='321 Pine St', telefono='3216549870'),
        Cliente(nombre='David Wilson', direccion='654 Cedar St', telefono='7891234560'),
    ]

    # Guardar los clientes en la base de datos
    for cliente in clientes:
        cliente.save()

    print("Se han insertado los clientes en la base de datos.")

if __name__ == "__main__":
    insertar_clientes()
