import os
import django
import random

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_imagine_apps.settings')
django.setup()

from logistics.models import Cliente, Transportista, Paquete

def asignar_paquetes():
    # Obtener clientes y transportistas existentes
    clientes = Cliente.objects.all()
    transportistas = Transportista.objects.all()

    # Verificar si hay suficientes clientes y transportistas
    if len(clientes) < 5 or len(transportistas) < 5:
        print("No hay suficientes clientes o transportistas en la base de datos.")
        return

    # Crear instancias de Paquete y asignarlos a clientes y transportistas
    for i in range(5):
        cliente = random.choice(clientes)
        transportista = random.choice(transportistas)
        peso = random.uniform(1, 10)
        dimensiones = "20x20x20"
        direccion_origen = "Origen #" + str(i+1)
        direccion_destino = "Destino #" + str(i+1)
        estado_entrega = "Pendiente"

        paquete = Paquete(
            cliente=cliente,
            transportista=transportista,
            peso=peso,
            dimensiones=dimensiones,
            direccion_origen=direccion_origen,
            direccion_destino=direccion_destino,
            estado_entrega=estado_entrega
        )
        paquete.save()

    print("Se han creado y asignado los paquetes a los clientes y transportistas existentes.")

if __name__ == "__main__":
    asignar_paquetes()
