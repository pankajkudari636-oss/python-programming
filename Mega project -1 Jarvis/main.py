import speech_recognition as sr
import pyttsx3
import webbrowser

import musicLibrary
# import pocketsphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    try:
        if "open google" in command.lower():
            webbrowser.open("https://google.com")
        elif "open.youtube" in command.lower():
             webbrowser.open("https://youtube.com")
        elif "open.whatsapp" in command.lower():
            webbrowser.open("https://whatsapp.com")
        elif "open.instagram"in command.lower():
            webbrowser.open("https://instagram.com")
        elif command.lower().startswith("play"):
                song = command.lower().split(" ",1)[1]
                link = musicLibrary.music[song]
                webbrowser.open(link)
        else:
            speak("Sorry, I don't know that song.")

    except IndexError:
        speak("Please tell me which song to play.")
if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        #obtain audio from the microphone 
        r = sr.Recognizer()
       

        # recognize speech using sphinx
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                    
                print("Listening....")
                audio = r.listen(source,timeout=5, phrase_time_limit=10)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                   print("Jarvis Active....")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)
                   processCommand(command)

        
        except Exception as e:
            print("Error:",e)
    
     



