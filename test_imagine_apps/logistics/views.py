from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cliente, Paquete, Transportista
from .forms import PackageForm

def package_send_by_client(request, cliente_id):
    client = get_object_or_404(Cliente, id=cliente_id)
    packages = Paquete.objects.filter(client=client)
    return render(request, 'package_send_by_client.html', {'client': client, 'packages': packages})


def carrier_assigned_packages(request, transportista_id):
    carrier = get_object_or_404(Transportista, id=transportista_id)
    packages = Paquete.objects.filter(carrier=carrier)
    return render(request, 'carrier_assigned_packages.html', {'carrier': carrier, 'packages': packages})


def create_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm()
    return render(request, 'create_package.html', {'form': form})


def edit_package(request, paquete_id):
    package = get_object_or_404(Paquete, id=paquete_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm(instance=package)
    return render(request, 'edit_package.html', {'form': form, 'package': package})


def delete_package(request, paquete_id):
    package = get_object_or_404(Paquete, id=paquete_id)
    if request.method == 'POST':
        package.delete()
        return redirect('package_list')
    return render(request, 'delete_package.html', {'package': package})


def package_list(request):
    packages = Paquete.objects.all()
    return render(request, 'package_list.html', {'packages': packages})


def clients_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clients_list.html', {'clientes': clientes})


# class PackageAssignView(APIView):
#     def put(self, request, paquete_id, transportista_id):
#         try:
#             package = Paquete.objects.get(id=paquete_id)
#             carrier = Transportista.objects.get(id=transportista_id)

#             package.carrier = carrier
#             package.save()

#             return Response({'message': 'Package assigned successfully'}, status=status.HTTP_200_OK)
#         except Paquete.DoesNotExist:
#             return Response({'message': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Transportista.DoesNotExist:
#             return Response({'message': 'Carrier does not exist'}, status=status.HTTP_404_NOT_FOUND)


# class PackageUpdateView(APIView):
#     def put(self, request, paquete_id):
#         try:
#             package = Paquete.objects.get(id=paquete_id)

#             new_status = request.data.get('estado_entrega')

#             if new_status in ['pendiente', 'en_transito', 'entregado']:
#                 package.estado_entrega = new_status
#                 package.save()

#                 return Response({'message': 'Delivery status updated successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Invalid delivery status'}, status=status.HTTP_400_BAD_REQUEST)
#         except Paquete.DoesNotExist:
#             return Response({'message': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

