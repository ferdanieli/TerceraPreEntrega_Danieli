from django import forms

from MiApp.models import Carrera, Commentarios


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = "__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Commentarios
        fields = ("usuario", "carrera", "comentario")



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