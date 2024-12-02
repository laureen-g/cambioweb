from django.shortcuts import render
import requests
import json
from cambioweb.form import Form

# Create your views here.

def home(request):

    cambios = busca_api()
    dados = json.loads(cambios.content.decode('utf-8'))
    choices = busca_moedas(dados['rates'])
    form = Form(choices=choices)


    return render(request, 'home.html', {'dados': dados, 'form': form})


def busca_api():
    url = "http://data.fixer.io/api/latest?access_key="
    api_key = '4e1f75ebad967e4c80af256ba3f9b2c4'

    response = requests.get(url+api_key)

    if response.status_code == 200:
        print("Resposta da API:", response.json)
    else:
        print("Erro de aquisição: ", response.status_code)

    return response

def busca_moedas(moedas):

    dic = {}

    for moeda in moedas:
        dic[moeda] = moeda

    return dic