#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import datetime

print("Welcome fellow humans.")

def desire():
  hour=datetime.datetime.now().hour
  if hour>=0 and hour<12:
    print("Good morning")
  elif hour>=0 and hour<18:
    print("Good afternoob")
  else:
    print("Good evening")

# This function obtain audio from microphone
def selfCommand():
  r = sr.Recognizer()
  with sr.Microphone as source:
    print("Listening.. ")
    audio = r.listen(source, offset=4, duration=5)
  try:
    statement=r.recognize_google(audio,language='en-in')
    print("Google: you said\n")
  # print("Google: you said\n" + sr.recognizer_google(audio))
  except Exception as e:
    print("Forgive me, please try again")
    return "None"
    
desire()
selfCommand()

# this function is still irrelevant 
class SelfSpeak():
  def __init__(self, speak):
    self = speak
    
# will need to make microphone work and computer say "print("Welcome fellow humans.")"
