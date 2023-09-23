import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
# Inicialize o reconhecedor de fala
reconhecedor = sr.Recognizer()

# Inicialize o motor de texto para fala
iniciar = pyttsx3.init()
iniciar.setProperty('rate', 150)

# Função para responder em voz alta
def responder(texto):
    print(texto)
    iniciar.say(texto)
    iniciar.runAndWait()

# Função principal do assistente virtual
def assistente():
    responder("Olá! Estou ouvindo. Como posso ajudar você?")

    while True:
        with sr.Microphone() as source:
            print("Ouvindo...")
            try:
                audio = reconhecedor.listen(source)
                entrada = reconhecedor.recognize_google(audio, language='pt-BR').lower()
                print(f"Você disse: {entrada}")
                
                if "olá" in entrada:
                    resposta = "Olá! Como posso ajudar você?"
                    responder(resposta)
                elif "fale sobre você" in entrada:
                    resposta = 'Sou a zaira assistente virtual do lucas'
                    responder(resposta)
                elif "acordada" in entrada:
                    resposta = "Pra você? Sempre!"
                    responder(resposta)

                elif "hora" in entrada:
                    resposta = "Agora são " + datetime.datetime.now().strftime("%H:%M:%S")
                    responder(resposta)

                elif "data" in entrada:
                    resposta = "Hoje é " + datetime.date.today().strftime("%d/%m/%Y")
                    responder(resposta)

                elif "abrir" in entrada:
                    site = entrada.split(" ")[-1]  # Extrair o último elemento da entrada
                    resposta = "Abrindo " + site
                    responder(resposta)
                    webbrowser.open(site)

                elif "calculadora" in entrada:
                    resposta = "Abrindo a calculadora."
                    responder(resposta)
                    os.system("calc")

                elif "desligar" in entrada:
                    resposta = "Desligando o computador."
                    responder(resposta)
                    os.system("shutdown /s /t 1")  # Desliga o computador em 1 segundo

                elif "reiniciar" in entrada:
                    resposta = "Reiniciando o computador."
                    responder(resposta)
                    os.system("shutdown /r /t 1")  # Reinicia o computador em 1 segundo

                elif "sair" in entrada:
                    resposta = "Saindo do assistente."
                    responder(resposta)
                    break

                else:
                    resposta = "Desculpe, não entendi o comando."
                    responder(resposta)

            except sr.UnknownValueError:
                print("Não entendi o que você disse.")
            except sr.RequestError as e:
                print(f"Erro no reconhecimento de fala; {e}")

if __name__ == "__main__":
    assistente()
