from django.shortcuts import render
from notafiscal.forms import NotaForms

def index(request):
    form = NotaForms()
    contexto = {'form': form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == "POST":
        form = NotaForms(request.POST)
        if form.is_valid():
            contexto = {'form': form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form Inválido')
            contexto = {'form': form}
            return render(request, 'index.html', contexto)
        