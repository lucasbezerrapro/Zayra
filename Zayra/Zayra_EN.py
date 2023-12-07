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
import sys  # Import sys module

# Initialize text to speech engine
start = pyttsx3.init()
start.setProperty('rate', 196)

# Function to respond out loud
def respond(text):
    print("\033[33m" + text + "\033[0m")
    start.say(text)
    start.runAndWait()

# Check the time
def current_temperature():
    api_key ='d78e9dff3b54bffa76bcdbe5acdd567f'

    city_name = 'Serra Talhada'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']

    if response.status_code == 200:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        respond(f'Current temperature in {city_name}: {temperature_celsius:.2f}°Celsius')
    else:
        respond(f'Error in API request: {data["message"]}')
    
# Function that will be executed when the button is clicked to end the program
def end_program():
    sys.exit()  # End the program

# Video to start
def play_audio_and_video():

        # Function to play the video
        def play_video():
            nonlocal video_path
            video_clip = VideoFileClip(video_path)
            pygame.display.set_caption("Video Playback")
            video_clip.preview()
            pygame.quit()

        # Load the audio (replace 'your_file.mp3' with the path of your MP3 file)
        audio_path = 'Zayra\StartSound.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)

        # Load the video (replace 'your_video.mp4' with the path of your video file)
        video_path = 'Zayra\starting.mp4'

        # Create a thread for video playback
        video_thread = threading.Thread(target=play_video)

        # Play the audio and start the video thread at the same time
        pygame.mixer.music.play()
        video_thread.start()
        video_thread.join()  # Wait for the video thread to finish

# IMPORTANT!!!!!!!!
# To make it more interesting, uncomment the functions below :)

def start_assistant():
    # Play when starting
    # play_audio_and_video()
    # Initialize speech recognizer
    
    
    recognizer = sr.Recognizer()


    system_starting = ['System started, components in order, what do you want to do first','Started and ready to work', 'Full energy. Today I'm inspired','I'm running, let's go']
    start_randomly = random.choice(system_starting)
    respond(start_randomly)

    while True:
        with sr.Microphone() as source:
            print("\033[32mListening\033[0m")
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=15, snowboy_configuration=None)
                input = recognizer.recognize_google(audio, language='pt-BR').lower() #Do you can change for english or your native language
                print(f"You said: {input}")

                if "are you there" in input:
                    respond("I'm here. Did you call me?")

                elif "work" in input or 'job' in input:
                    answers = ['And the pix is still nothing. AN', 'When you pay me a salary we talk','In my time, we worked with pix and I was created this year']
                    random_answer = random.choice(answers)
                    respond(random_answer)

                elif 'yes' in input or 'I called' in input:
                    respond('Tell me what you want me to do')

                elif "tell about you" in input:
                    respond(
                        'I am Zaira, Lucas' virtual assistant. I make jokes and research of any intellectual level. I am jack of all trades')

                # List of thanks
                elif "thank you" in input or 'thanks' in input:
                    responses = ["You're welcome", "At your service", "Anything else, sir?", "If you need, we are together","Without me, you can't do anything anyway, hahahaha"]
                    random_response = random.choice(responses)
                    respond(random_response)

                elif "awake" in input:
                    responses = ["For you? Always!", "I was sleeping dreaming of a salary","I was almost. What's new?"]
                    random_response = random.choice(responses)
                    respond(random_response)

                elif "are you deaf" in input:
                    respond('You don't even pay me a salary and you're nagging')

                elif "week" in input:
                    respond('Happy week in the peace of God, to all of the Adventist group of Varzinha')
                elif 'today' in input:
                    # Get the current day of the week
                    day_of_the_week = datetime.datetime.now().weekday()

                    # Map the day of the week number to the day name
                    match day_of_the_week:
                        case 0:
                            day_name = "Monday"
                        case 1:
                            day_name = "Tuesday"
                        case 2:
                            day_name = "Wednesday"
                        case 3:
                            day_name = "Thursday"
                        case 4:
                            day_name = "Friday"
                        case 5:
                            day_name = "Saturday"
                        case _:
                            day_name = "Sunday"
                    respond('Today is ' + day_name)
                    
                elif "time" in input:
                    respond("It's now " + datetime.datetime.now().strftime("%H:%M:%S"))
                elif "date" in input:
                    respond("Today is " + datetime.date.today().strftime("%d/%m/%Y"))
                elif "search" in input or 'research' in input:
                    site = input.split(" ")[-1]  # Extract the last element of the input
                    respond("Opening " + site)
                    webbrowser.open(site)
                elif "calculator" in input:
                    respond("Opening the calculator.")
                    os.system("calc")
                elif "shutdown" in input:
                    respond("Shutting down the computer.")
                    os.system("shutdown /s /t 1")
                    
                elif "temperature" in input:
                    current_temperature()
                    
                elif "restart" in input:
                    respond("Restarting the computer.")
                    os.system("shutdown /r /t 1")

                elif "exit" in input or "end" in input:
                    respond("Ending the assistant.")
                    break
                else:
                    respond("Sorry, I didn't understand the command.")

            except sr.UnknownValueError:
                print("I didn't understand what you said.")
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")

def start_program():

    window.destroy()

def start_program():
    window = tk.Tk()
    window.geometry('400x400')
    window.title('Zayra Assistant')  # Add a title to the window

    # Change the window color to yellow
    window.configure(bg='black')

# Load an image
    image = Image.open("Zayra/logo.jpg")  # Replace with the correct path of your image
    image = image.resize((400, 400))  # Resize the image to 400x330
    image = ImageTk.PhotoImage(image)

    # Create a canvas to display the image
    canvas = tk.Canvas(window, width=400, height=400, bg='black')
    canvas.pack()

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    # Add buttons to the canvas
    button = tk.Button(canvas, text='Start Zayra', command=start_assistant, bg='orange')
    button_window = canvas.create_window(165, 310, anchor=tk.NW, window=button)

    exit_button = tk.Button(canvas, text='Exit assistant', command=end_program, bg='orange')
    exit_button_window = canvas.create_window(153, 350, anchor=tk.NW, window=exit_button)

    window.mainloop()

# Call the start_program function to start the interface
start_program()

