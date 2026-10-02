import speech_recognition as sr
import webbrowser

import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3
import pyttsx3nit()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif command.lower().startswith("play"):
        song = command.lower().split("")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            word = r.recognize_google(audio)

            print("You said:", word)

            if word.lower() == "jarvis":
                speak("Yaa")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", e)