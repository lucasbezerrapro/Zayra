"""
  Essa parte separada sempre para fazer varios testes de logica do programa.
  caso esteja aqui para contribuir, use e abuse deste espaço.
  Para que o programa principal não fique poluido ;)

"""



import requests
import pyttsx3
iniciar = pyttsx3.init()
iniciar.setProperty('rate', 196)

  # Função para responder em voz alta
def responder(texto):
  print("\033[33m" + texto + "\033[0m")
  iniciar.say(texto)
  iniciar.runAndWait()
chave_api ='d78e9dff3b54bffa76bcdbe5acdd567f'

nome_cidade = 'Serra Talhada'

url=f'https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api}'

response = requests.get(url)
data = response.json()

temperatura = data['main']['temp']

if response.status_code == 200:
    temperatura_kelvin = data['main']['temp']
    temperatura_celsius = temperatura_kelvin - 273.15
    responder(f'Temperatura atual em {nome_cidade}: {temperatura_celsius:.2f}°Celsius')
else:
    responder(f'Erro na solicitação à API: {data["message"]}')
    
    