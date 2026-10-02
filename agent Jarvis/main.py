import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse
import ollama


# =====================================================
# SETUP
# =====================================================

recognizer = sr.Recognizer()

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# =====================================================
# SPEAK
# =====================================================

def speak(text):

    print("JARVIS:", text)

    engine.say(text)
    engine.runAndWait()


# =====================================================
# LISTEN
# =====================================================

def listen():

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        command = command.lower().strip()

        print("YOU:", command)

        return command

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("I could not understand.")
        return ""

    except sr.RequestError as e:

        print("Google speech service error:", e)
        return ""

    except Exception as e:

        print("Microphone error:", e)
        return ""


# =====================================================
# AI
# =====================================================

def ask_ai(question):

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content":
                    "You are Jarvis. Answer briefly in 1 or 2 sentences."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"].strip()

    except Exception as e:

        print("AI ERROR:", e)

        return "Sorry Pankaj, my AI brain is not available."


# =====================================================
# COMMAND PROCESSOR
# =====================================================

def process_command(command):

    command = command.lower().strip()

    print("COMMAND RECEIVED:", command)


    # -----------------------------
    # STOP JARVIS
    # -----------------------------

    if command in [
        "stop jarvis",
        "exit jarvis",
        "quit jarvis"
    ]:

        speak("Goodbye Pankaj.")

        return False


    # -----------------------------
    # RADHA RADHA
    # -----------------------------

    if "radha radha" in command:

        speak("Radha Radha")

        return True


    # -----------------------------
    # GOOGLE
    # -----------------------------

    if "open google" in command:

        speak("Opening Google.")

        webbrowser.open(
            "https://www.google.com"
        )

        return True


    # -----------------------------
    # YOUTUBE
    # -----------------------------

    if "open youtube" in command:

        speak("Opening YouTube.")

        webbrowser.open(
            "https://www.youtube.com"
        )

        return True


    # -----------------------------
    # INSTAGRAM
    # -----------------------------

    if "open instagram" in command:

        speak("Opening Instagram.")

        webbrowser.open(
            "https://www.instagram.com"
        )

        return True


    # -----------------------------
    # WHATSAPP
    # -----------------------------

    if "open whatsapp" in command:

        speak("Opening WhatsApp.")

        webbrowser.open(
            "https://web.whatsapp.com"
        )

        return True


    # -----------------------------
    # GOOGLE SEARCH
    # -----------------------------

    if command.startswith("search google for"):

        query = command.replace(
            "search google for",
            "",
            1
        ).strip()

        if query:

            speak("Searching Google.")

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote_plus(query)
            )

            webbrowser.open(url)

        return True


    # -----------------------------
    # PLAY SONG
    # -----------------------------

    if command.startswith("play "):

        song = command[5:].strip()

        if song:

            speak("Playing " + song)

            url = (
                "https://www.youtube.com/results?search_query="
                + urllib.parse.quote_plus(song)
            )

            webbrowser.open(url)

        return True


    # -----------------------------
    # AI QUESTION
    # -----------------------------

    answer = ask_ai(command)

    speak(answer)

    return True


# =====================================================
# MAIN
# =====================================================

def main():

    print()
    print("=" * 50)
    print("             JARVIS AI ASSISTANT")
    print("=" * 50)
    print()

    speak(
        "System online. I am Jarvis, Pankaj's personal AI assistant."
    )

    print()
    print("Jarvis is ready.")
    print()
    print("Say: Jarvis")
    print()


    while True:

        # ---------------------------------------------
        # WAIT FOR JARVIS
        # ---------------------------------------------

        word = listen()

        if not word:
            continue


        if "jarvis" in word:

            speak(
                "Yes Pankaj, I am listening."
            )


            # -----------------------------------------
            # LISTEN FOR COMMAND
            # -----------------------------------------

            command = listen()

            if not command:
                continue


            # -----------------------------------------
            # RUN COMMAND
            # -----------------------------------------

            result = process_command(command)

            if result is False:

                print("Jarvis stopped.")

                break


# =====================================================
# START
# =====================================================

if __name__ == "__main__":

    main()