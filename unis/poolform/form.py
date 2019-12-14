from django import forms

class myForm(forms.Form):
    nome = forms.CharField(max_length=150)
    endereco = forms.CharField(max_length=150)
    peso = forms.CharField(max_length=15)
    altura = forms.CharField(max_length=15)
    imc = forms.CharField(max_length=150)