import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import asyncio

# Inicialize o reconhecedor de fala
reconhecedor = sr.Recognizer()
# Inicialize o motor de texto para fala
iniciar = pyttsx3.init()
iniciar.setProperty('rate', 190)

# Função para responder em voz alta
async def responder(texto):
    print(texto)
    iniciar.say(texto)
    iniciar.runAndWait()

# Função principal do assistente virtual
async def assistente():
    await responder("Ligando motores, zayra está funcionando, diga algo para que eu possa fazer")

    while True:
        with sr.Microphone() as source:
            print("Ouvindo...")
            try:
                audio = reconhecedor.listen(source)
                entrada = reconhecedor.recognize_google(audio, language='pt-BR').lower()
                print(f"Você disse: {entrada}")

                if "olá" in entrada:
                    await responder("Olá! Como posso ajudar você?")
                elif "fale sobre você" in entrada:
                    await responder('Sou a zaira assistente virtual do lucas')
                #lista de agradecimentos
                elif "obrigado" in entrada or 'obrigada' in entrada:
                    respostas = ["De nada", "Disponha", "mais alguma coisa senhor", "precisando tamo junto", "Sem mim você nada faz mesmo kkkkkkkkkkkk"]
                    resposta_aleatoria = random.choice(respostas)
                    await responder(resposta_aleatoria)
                    
                elif "acordada" in entrada:
                    respostas = ["Pra você? Sempre!", "estava dormindo sonhandom com um salario", "Estava quase. Qua a boa?"]
                    resposta_aleatoria = random.choice(respostas)
                    await responder(resposta_aleatoria)
                elif "tá surdo" in entrada or "tá surda" in entrada:
                    await responder('nem me paga salário e fica de larica')
                
                
                elif "semana" in entrada:
                    await responder('Feliz semana na paz de Deus, a, todos do grupo adventista de varzinha')
                elif 'hoje' in entrada:
                    # Obtenha o dia da semana atual
                    dia_da_semana = datetime.datetime.now().weekday()

                    # Mapeie o número do dia da semana para o nome do dia
                    if dia_da_semana == 0:
                        nome_do_dia = "Segunda-feira"
                    elif dia_da_semana == 1:
                        nome_do_dia = "Terça-feira"
                    elif dia_da_semana == 2:
                        nome_do_dia = "Quarta-feira"
                    elif dia_da_semana == 3:
                        nome_do_dia = "Quinta-feira"
                    elif dia_da_semana == 4:
                        nome_do_dia = "Sexta-feira"
                    elif dia_da_semana == 5:
                        nome_do_dia = "Sábado"
                    else:
                        nome_do_dia = "Domingo"
                    await responder('Hoje é ' + nome_do_dia)
                elif "horas" in entrada:
                    await responder("Agora são " + datetime.datetime.now().strftime("%H:%M:%S"))
                elif "data" in entrada:
                    await responder("Hoje é " + datetime.date.today().strftime("%d/%m/%Y"))
                elif "abrir" or 'abra' in entrada:
                    site = entrada.split(" ")[-1]  # Extrair o último elemento da entrada
                    await responder("Abrindo " + site)
                    webbrowser.open(site)
                elif "calculadora" in entrada:
                    await responder("Abrindo a calculadora.")
                    os.system("calc")
                elif "desligar" in entrada:
                    await responder("Desligando o computador.")
                    os.system("shutdown /s /t 1")
                elif "reiniciar" in entrada:
                    await responder("Reiniciando o computador.")
                    os.system("shutdown /r /t 1")
                    
                elif "sair" or "encerrar" in entrada:
                    await responder("Saindo do assistente.")
                    break
                
                else:
                    await responder("Desculpe, não entendi o comando.")
                    
            except sr.UnknownValueError:
                print("Não entendi o que você disse.")
            except sr.RequestError as e:
                print(f"Erro no reconhecimento de fala; {e}")

if __name__ == "__main__":
    asyncio.run(assistente())
