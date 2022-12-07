#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
# import wolframalpha
import datetime

print("Welcome!")

input_user = input("Say something: ")

engine = pyttsx3.init()
# GivenSpeech = "I’m increasingly inclined to think that there should be some regulatory oversight, maybe at the national and international level, just to make sure that we don’t do something very foolish. I mean with artificial intelligence we’re summoning the demon"

# will need to make input_user speak when user run program 
'''
def UserInputSpeak():
  engine.say()
  engine.runAndWait()
'''

engine.setProperty('voice', 'voices[0].id')

def speak(text):
  engine.say(text)
  engine.runAndWait()

def wishMe():
  hour=datetime.datetime.now().hour
  if hour>=0 and hour<12:
  # speak("Hello, Good Morning")
    print("Hello, Good Morning")
  elif hour>=12 and hour<12:
  # speak("Hello, Good Afternoon")
    print("Hello, Good Afternoon")
  else:
  # speak("Hello, Good Evening")
    print("Hello, Good Evening")

def speakCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
    print("Listening...")
    audio=r.listen(source)

rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate", 180)

# speak(GivenSpeech) # say these words slower
# UserInputSpeak(input_user)
speak("Hello, user!")
wishMe()

#speak(input_user) - Did not work
