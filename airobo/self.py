#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
#import comtypes

print("Welcome fellow humans.") #sample response

def speak(text):
  engine.say(text)
  engine.runAndWait()

# This function obtain audio from microphone
# def selfCommand():
  r = sr.Recognizer()
  with sr.Microphone as source:
    print("Listening.. ")
    audio = r.listen(source, offset=4, duration=5)
  try:
    statement=r.recognize_google(audio,language='en-in')
    print("Google: you said\n")
  # print("Google: you said\n" + sr.recognizer_google(audio))
  except:
    print("An exception occured")

# this function is still irrelevant 
class SelfSpeak():
  def __init__(self, speak):
    self = speak
    
# will need to make microphone work and computer say "print("Welcome fellow humans.")"
