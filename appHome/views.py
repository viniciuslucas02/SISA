from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from .models import Usuario
import requests
import json
from datetime import datetime

from django.http import HttpResponse



def appHome(request):
    return render(request, 'appHome/home.html')

# -------------------------------------------------------------------
@csrf_exempt
def cadastrar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        
        if not url:
            print("⚠️ Nenhum URL recebido")
            return JsonResponse({'error': 'Nenhum URL enviado'})

        print(f"📡 QR Code detectado: {url}")

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
               
            dados = {}
            for tr in soup.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) == 2:
                    chave = tds[0].get_text(strip=True)
                    valor = tds[1].get_text(strip=True)
                    dados[chave] = valor              

            if Usuario.objects.filter(nome=dados.get('Para', '')).exists():
                print("Usuário já cadastrado")

            else:
                
                data_str = dados.get("Emitido em", "").strip('“”')
                data_formatada = datetime.strptime(data_str, "%d/%m/%y").date()

                usuario = Usuario(
                    nome=dados.get('Para', ''),
                    faculdade=dados.get('Faculdade', ''),
                    curso=dados.get('Curso', ''),
                    turno=dados.get('Turno', ''),
                    emitido=data_formatada
                )
                usuario.save()
                print("Página acessada com sucesso:")

                for chave, valor in dados.items():
                    print(f"  {chave}: {valor}")

            return render(request, 'appHome/home.html', {'dados': dados})

        except Exception as e:
            print(f"❌ Erro ao processar o URL: {e}")
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Método não permitido'}, status=405)

# -------------------------------------------------------------------