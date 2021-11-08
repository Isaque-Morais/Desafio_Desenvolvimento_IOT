from django import forms
from tempus_dominus.widgets import DatePicker
from notafiscal.tipos_notas import tipos_de_notas
from notafiscal.validacao import *

class NotaForms(forms.Form):
    numero = forms.CharField(label='Nº da nota:', max_length=100)
    cnpj = forms.CharField(label='CNPJ:', max_length=100)
    mercado = forms.CharField(label='Mercado:', disabled=True, initial="IOT")
    valor_compra = forms.CharField(label='Valor da compra:')
    data = forms.DateField(label='Data:', widget=DatePicker())
    entidade = forms.CharField(label='Entidade de caridade:')
    tipos_nota = forms.ChoiceField(label='Tipo de nota', choices=tipos_de_notas)


    def clean(self):
        numero =self.cleaned_data.get("numero")
        cnpj =self.cleaned_data.get('cnpj')
        lista_de_erros = {}
        campo_tem_alguma_letra(numero, 'numero', lista_de_erros)
        campo_tem_alguma_letra(cnpj, 'cnpj', lista_de_erros)
        numero_cnpj_iguais(numero, cnpj, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data