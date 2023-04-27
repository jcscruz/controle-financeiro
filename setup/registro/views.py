from django.shortcuts import render

from registro.models import Registro_Financeiro

def index(request):
        return render(request, 'registro/index.html')

def cadastro(request):
        dados = Registro_Financeiro.objects.all()
        return render(request, 'registro/cadastro.html', {"registros": dados})