from django.shortcuts import render, get_object_or_404, redirect
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
