from django import forms
from posiciones.models import Categoria, Competidor, Equipo, Carrera, CarrEqui


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class CompetidorForm(forms.ModelForm):
    class Meta:
        model = Competidor
        fields = '__all__'


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'


class CarreraEquipoForm(forms.ModelForm):
    class Meta:
        model = CarrEqui
        fields = '__all__'
