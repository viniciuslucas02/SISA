from django.shortcuts import render

#importe a classe HttpResponse ao módulo http dentro do pacote django
from django.http import HttpResponse

#função que cria a view que exibe a mensagem "Olá mundo"

def appHome(request):
    return render(request, 'appHome/home.html')
