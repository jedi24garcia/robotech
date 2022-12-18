#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

print("Hello, user!")
newVoiceRate = 150

engine = pyttsx3.init()
engine.setProperty("voice", "voices[1].id")
engine.setProperty("rate", newVoiceRate)

def speak(text):
  engine.say(text)
  engine.runAndWait()

# depending on the time, computer will say greetings below:
def wishGreetings():
  hour=datetime.datetime.now().hour    
  if hour>=0 and hour<12:
    speak("Good Morning")
  elif hour>=12 and hour<18:
    speak("Good Afternoon")
  else:
    speak("Good Evening")

def TakeCommands():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    
    try:
       statement = r.recognize_google(audio,language='en-in')
       print(f"user said:{statement}\n")

    except Exception as e:
       speak("Can you please repeat that again?")
       return "None"
    return statement

speak("Ready for your command ser")
wishGreetings()


if __name__ == "__main__":

  while True:
    speak("How can I help?")
    statement = TakeCommands().lower()
    if statement == 0:
      continue

# TODO: Remember same issue with AI-Personal Voice
# TODO: AttributeError: module 'speech_recognition' has no attribute 'Microphone'

# TODO: Follow step:
"""
These steps worked on M1 Pro chips

Install portaudio
brew install portaudio
Link portaudio
brew link portaudio
Copy the path where portaudio was installed (use it in the next step)
brew --prefix portaudio
Create .pydistutils.cfg in your home directory
sudo nano $HOME/.pydistutils.cfg
then paste the following

[build_ext]
include_dirs=<PATH FROM STEP 3>/include/
library_dirs=<PATH FROM STEP 3>/lib/

Install pyaudio
pip install pyaudio

or

pip3 install pyaudio
"""
