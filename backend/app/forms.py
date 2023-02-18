from django import forms
from backend import settings

class HermanaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)

class PrimaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)

class TiaFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)