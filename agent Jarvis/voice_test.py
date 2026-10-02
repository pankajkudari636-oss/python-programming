import pyttsx3

print("Starting voice test...")

engine = pyttsx3.init("sapi5")

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

print("Available voices:")

for i, voice in enumerate(voices):
    print(i, voice.name)

print("\nTesting Jarvis voice...")

engine.say("Hello Pankaj. This is Jarvis. Can you hear me?")
engine.runAndWait()

print("Voice test finished.")