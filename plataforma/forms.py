from django import forms

class Cliente(forms.Form):
    nome = forms.CharField(max_length=100)
    idade = forms.IntegerField()