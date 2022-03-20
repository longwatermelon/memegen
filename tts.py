import pyttsx3
import sys

print("tts start")
engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.save_to_file(sys.argv[1], f"tts.mp3")
engine.runAndWait()

print("tts done")