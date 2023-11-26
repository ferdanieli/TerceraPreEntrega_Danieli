from django import forms

class CarreraForm(forms.Form):
    nombre = forms.CharField()
    comisión = forms.IntegerField()


class BuscarCarreraForm(forms.Form):
    nombre = forms.CharField()