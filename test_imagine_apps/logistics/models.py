from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Transportista(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=50)
    contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Paquete(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    direccion_origen = models.CharField(max_length=200)
    direccion_destino = models.CharField(max_length=200)
    estado_entrega = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='paquetes_enviados')
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, related_name='paquetes_asignados')

    def __str__(self):
        return f"Paquete #{self.id}"
