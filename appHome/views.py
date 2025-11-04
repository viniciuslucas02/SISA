from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests
import json

from django.http import HttpResponse



def appHome(request):
    return render(request, 'appHome/home.html')

@csrf_exempt
def cadastrar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        if not url:
            print("⚠️ Nenhum URL recebido")  # aparece no terminal
            return JsonResponse({'error': 'Nenhum URL enviado'})

        print(f"📡 QR Code detectado: {url}")  # <-- mostra no terminal

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'Sem título'
               
            dados = {}
            for tr in soup.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) == 2:
                    chave = tds[0].get_text(strip=True)
                    valor = tds[1].get_text(strip=True)
                    dados[chave] = valor                

            # Exibe os dados no terminal
            print("🌐 Página acessada com sucesso:")
            print(f"➡️ URL: {url}")
            print(f"📄 Título: {title}")

            for chave, valor in dados.items():
                print(f"  {chave}: {valor}")

            return JsonResponse({'url': url, 'title': title, 'dados':dados})

        except Exception as e:
            print(f"❌ Erro ao processar o URL: {e}")
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Método não permitido'}, status=405)