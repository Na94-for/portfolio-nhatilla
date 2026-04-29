import requests

# Configurações
API_KEY = "ad16f2125adcbe128b487d7b49179e23"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def consultar_clima(cidade):
    # Monta os parâmetros da requisição
    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    # Faz a requisição à API
    resposta = requests.get(BASE_URL, params=parametros)
    dados = resposta.json()

    # Verifica se a cidade foi encontrada
    if resposta.status_code == 200:
        print(f"\n📍 Cidade: {dados['name']}, {dados['sys']['country']}")
        print(f"🌡️  Temperatura: {dados['main']['temp']}°C")
        print(f"🤔 Sensação térmica: {dados['main']['feels_like']}°C")
        print(f"💧 Umidade: {dados['main']['humidity']}%")
        print(f"🌤️  Clima: {dados['weather'][0]['description']}")
    else:
        print(f"\n❌ Erro: {dados['message']}")

# Pede o nome da cidade para o usuário
cidade = input("Digite o nome da cidade: ")
consultar_clima(cidade)