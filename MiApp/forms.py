from django import forms

class CarreraForm(forms.Form):
    nombre = forms.CharField()
    comisión = forms.IntegerField()


class BuscarCarreraForm(forms.Form):
    nombre = forms.CharField()

class DirectorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class BuscarDirectorForm(forms.Form):
    nombre = forms.CharField()

class MateriaForm(forms.Form):
    nombre = forms.CharField()
    puntos = forms.IntegerField()

class BuscarMateriaForm(forms.Form):
    nombre = forms.CharField()