import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import threading
from moviepy.editor import VideoFileClip
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import requests
import sys  # Importe o módulo sys



# Inicialize o motor de texto para fala
iniciar = pyttsx3.init()
iniciar.setProperty('rate', 196)

    # Função para responder em voz alta
def responder(texto):
    print("\033[33m" + texto + "\033[0m")
    iniciar.say(texto)
    iniciar.runAndWait()

#verificar o tempo
def temperatura_atual():
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
    
# Função que será executada quando o botão for clicado para encerrar o programa
def encerrar_programa():
    sys.exit()  # Encerre o programa

#video para inicializar
def reproduzir_audio_e_video():


        # Função para reproduzir o vídeo
        def reproduzir_video():
            nonlocal video_path
            video_clip = VideoFileClip(video_path)
            pygame.display.set_caption("Reprodução de Vídeo")
            video_clip.preview()
            pygame.quit()

        # Carregue o áudio (substitua 'seu_arquivo.mp3' pelo caminho do seu arquivo MP3)
        audio_path = 'Zayra\StartSound.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)

        # Carregue o vídeo (substitua 'seu_video.mp4' pelo caminho do seu arquivo de vídeo)
        video_path = 'Zayra\iniciando.mp4'

        # Crie uma thread para a reprodução do vídeo
        video_thread = threading.Thread(target=reproduzir_video)

        # Reproduza o áudio e inicie a thread do vídeo ao mesmo tempo
        pygame.mixer.music.play()
        video_thread.start()
        video_thread.join()  # Aguarde a thread do vídeo terminar

#IMPORTANTE!!!!!!!!
#Para melhor deixar mais interessante tirre o comentario das funçoes abaixo :)

def iniciar_assistente():
    #reproduzir ao iniciar
    #reproduzir_audio_e_video()
    # Inicialize o reconhecedor de fala
    
    
    reconhecedor = sr.Recognizer()


    sistema_iniciando = ['Sistema iniciado, componentes em ordem, o que quer fazer primeiro','Iniciada e pronta para trabalhar', 'Energia total. Hoje estou inspirada','Estou rodando, vamos lá']
    iniciar_aleatoriamente = random.choice(sistema_iniciando)
    responder(iniciar_aleatoriamente)

    while True:
        with sr.Microphone() as source:
            print("\033[32mOuvindo\033[0m")
            try:
                audio = reconhecedor.listen(source, timeout=10, phrase_time_limit=15, snowboy_configuration=None)
                entrada = reconhecedor.recognize_google(audio, language='pt-BR').lower()
                print(f"Você disse: {entrada}")

                if "está ai" in entrada:
                    responder("Estou aqui. Você me chamou?")

                elif "trabalhar" in entrada or 'trabalho' in entrada:
                    respostas = ['E o pix nada ainda. AN', 'Quando me pagar um salário nós conversa','No meu tempo, nós trabalhava com pix e eu fui criada esse ano']
                    resposta_aleatoria = random.choice(respostas)
                    responder(resposta_aleatoria)

                elif 'sim' in entrada or 'chamei' in entrada:
                    responder('Me fale o que quer que eu faça')

                elif "fale sobre você" in entrada:
                    responder(
                        'Sou a Zaira, assistente virtual do Lucas. Faço piadas e pesquisas de qualquer nível intelectual. Sou pau pra toda obra')

                # Lista de agradecimentos
                elif "obrigado" in entrada or 'obrigada' in entrada:
                    respostas = ["De nada", "Disponha", "Mais alguma coisa, senhor?", "Precisando, estamos juntos","Sem mim, você não faz nada mesmo, kkkkkkkkkkkk"]
                    resposta_aleatoria = random.choice(respostas)
                    responder(resposta_aleatoria)

                elif "acordada" in entrada:
                    respostas = ["Pra você? Sempre!", "Estava dormindo sonhando com um salário","Estava quase. O que há de novo?"]
                    resposta_aleatoria = random.choice(respostas)
                    responder(resposta_aleatoria)

                elif "tá surdo" in entrada or "tá surda" in entrada:
                    responder('Nem me paga salário e fica de larica')

                elif "semana" in entrada:
                    responder('Feliz semana na paz de Deus, a todos do grupo adventista de Varzinha')
                elif 'hoje' in entrada:
                    # Obtenha o dia da semana atual
                    dia_da_semana = datetime.datetime.now().weekday()

                    # Mapeie o número do dia da semana para o nome do dia
                    match dia_da_semana:
                        case 0:
                            nome_do_dia = "segunda"
                        case 1:
                            nome_do_dia = "Terça-feira"
                        case 2:
                            nome_do_dia = "Quarta-Feira"
                        case 3:
                            nome_do_dia = "Quinta-Feira"
                        case 4:
                            nome_do_dia = "Sexta-Feira"
                        case 5:
                            nome_do_dia = "Sabado"
                        case _:
                            nome_do_dia = "Domingo"
                    responder('Hoje é ' + nome_do_dia)
                    
                elif "horas" in entrada:
                    responder("Agora são " + datetime.datetime.now().strftime("%H:%M:%S"))
                elif "data" in entrada:
                    responder("Hoje é " + datetime.date.today().strftime("%d/%m/%Y"))
                elif "pesquise" in entrada or 'pesquisar' in entrada:
                    site = entrada.split(" ")[-1]  # Extrair o último elemento da entrada
                    responder("Abrindo " + site)
                    webbrowser.open(site)
                elif "calculadora" in entrada:
                    responder("Abrindo a calculadora.")
                    os.system("calc")
                elif "desligar" in entrada:
                    responder("Desligando o computador.")
                    os.system("shutdown /s /t 1")
                    
                elif "temperatura" in entrada:
                    temperatura_atual()
                    
                elif "reiniciar" in entrada:
                    responder("Reiniciando o computador.")
                    os.system("shutdown /r /t 1")

                elif "sair" in entrada or "encerrar" in entrada:
                    responder("Encerrando o assistente.")
                    break
                else:
                    responder("Desculpe, não entendi o comando.")

            except sr.UnknownValueError:
                print("Não entendi o que você disse.")
            except sr.RequestError as e:
                print(f"Erro no reconhecimento de fala: {e}")

def iniciar_programa():

    janela.destroy()

def iniciar_programa():
    janela = tk.Tk()
    janela.geometry('400x400')
    janela.title('Zayra Assistente')  # Adicione um título à janela

    # Alterar a cor da janela para amarelo
    janela.configure(bg='black')

    # Carregar uma imagem
    imagem = Image.open("Zayra/logo.jpg")  # Substitua pelo caminho correto da sua imagem
    imagem = imagem.resize((400, 400))  # Redimensione a imagem para 400x330
    imagem = ImageTk.PhotoImage(imagem)

    # Criar um canvas para exibir a imagem
    canvas = tk.Canvas(janela, width=400, height=400, bg='black')
    canvas.pack()

    # Exibir a imagem no canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=imagem)
    
    # Adicionar botões ao canvas
    button = tk.Button(canvas, text='Iniciar Zayra', command=iniciar_assistente, bg='orange')
    button_window = canvas.create_window(165, 310, anchor=tk.NW, window=button)

    button_sair = tk.Button(canvas, text='Sair do assistente', command=encerrar_programa, bg='orange')
    button_sair_window = canvas.create_window(153, 350, anchor=tk.NW, window=button_sair)

    janela.mainloop()

# Chame a função iniciar_programa para iniciar a interface
iniciar_programa()