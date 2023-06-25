from django import forms
from .models import Paquete


class PackageForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = '__all__'

