#!/usr/bin/env python3

import speech_recognition as sr  # version 3.9.0
import pyttsx3
import wikipedia
import datetime
import pyaudio
import pyttsx3
import time 
import sys
from AppKit import NSSpeechSynthesizer

password = "admiral"

while True:
  user_input = input("Please enter password: ")
  if user_input == password:
    break
  else:
    print("Wrong! Please try again!")

print("Hello, user!")
newVoiceRate = 170

engine = pyttsx3.init("nsss")
engine.setProperty("voice", "voices[1].id")
engine.setProperty("rate", newVoiceRate)

# add class NSSpeechDriver here

def speak(text):
  engine.say(text)
  engine.runAndWait()

# depending on the time, computer will say greetings below:
def wishGreetings():
  hour=datetime.datetime.now().hour    
  if hour>=0 and hour<12:
    speak("Good Morning")
    print("Good Morning")
  elif hour>=12 and hour<18:
    speak("Good Afternoon")
    print("Good Afternoon")
  else:
    speak("Good Evening") 
    print("Good Evening")

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
    print("How can I help?")
    statement = TakeCommands().lower()
    if statement == 0:
      continue
    
    if "Ok bye" in statement or "stop" in statement:
      speak("Bye bye now")
      print("Bye bye now")
      break

    elif "Logging off now" in statement or "signing out" in statement:
      speak("Okay, terminating machine now")
      subprocess.call(["Shutdown"])

time.sleep(5)
