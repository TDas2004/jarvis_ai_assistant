import speech_recognition as sr
import pyaudio
import pyttsx3
import time
import webbrowser
from client import ask_openai


recognizer = sr.Recognizer()
engine = pyttsx3.init()

wake_word = "jarvis"


def speak(text):
 engine.say(text)
 engine.runAndWait()


def listen_for_wake_word():
 with sr.Microphone() as source:
    print("listen for wake word")

    print(" adjusting background noise")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("listenning")
    audio = recognizer.listen(source)

    try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command == wake_word
    except sr.UnknownValueError:
            return False
    
def listen_for_command():
    with sr.Microphone() as source:
        print("listenning command")
        recognizer.adjust_for_ambient_noise(source)
        try:
         audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        except:
            speak("timed out")
            return 
        

    try:

        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        speak(f"initializing command: {command}")

        if "open" in command.lower():
            site = command.replace("open ", "").strip()
            if "." not in site:
                site += ".com"
            url = "https://" + site
            webbrowser.open(url)

        elif "search" in command.lower():
            query = command.lower().split("search" , 1)[1].strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        else:
            ai_response = AIprocess(command)  # ← Let Jarvis respond
            print("Jarvis:", ai_response)
            speak(ai_response)            

    except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")  

def AIprocess(command):
    try:
        response = ask_openai(command)  # pass the user's question
        return response
    except Exception as e:
        speak("Some error happened in processing your request.")
        print("Error:", e)


while True:
     if listen_for_wake_word():
        speak("yes, how can i help")
        listen_for_command()
        time.sleep(1)

