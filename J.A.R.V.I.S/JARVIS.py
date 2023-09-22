import pyttsx3
import speech_recognition as sr


iniciar = pyttsx3.init()
iniciar.setProperty('rate', 150)  # Velocidade da fala (opcional)
iniciar.say("bem vindao ao seu assistente virtual, eu sou a assistente virtual do lucas, a zayra.")
iniciar.runAndWait()
# Inicialize o reconhecedor
reconhecimento = sr.Recognizer()
# Use um microfone como fonte de áudio
with sr.Microphone() as source:
    print("Iniciando gravação. Fale algo...")
    try:
        audio = reconhecimento.listen(source)
        print("Gravação concluída. Aguardando reconhecimento...")
        # Reconheça a fala usando o Google Web Speech API
        texto = reconhecimento.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError as e:
        print(f"Erro no reconhecimento de fala; {e}")
        
    iniciar = pyttsx3.init()
    iniciar.setProperty('rate', 150)  # Velocidade da fala (opcional)
    if texto == 'Olá':
      iniciar.say(f'bem vindo Senhor , oque posso fazer pelo senhor?')
    elif texto == 'acordada':
      iniciar.say('para você sempre, diga oque precisa Senhor')
    elif texto =='como vai':
      iniciar.say('sim, obrigado por perguntar')
iniciar.runAndWait()