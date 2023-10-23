# En tu archivo forms.py
from django import forms
from .models import Partido

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['fecha', 'hora', 'ubicacion']
