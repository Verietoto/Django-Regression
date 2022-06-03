from django import forms

class Regresi_form(forms.Form):
    x = forms.DecimalField(label="Nilai X")
    y = forms.DecimalField(label="Nilai Y")