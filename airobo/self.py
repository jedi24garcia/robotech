#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import datetime

print("Welcome humans.")

User_Input = input("Please enter your message here: ")

selfResponse = ("How are you?")

def desire():
  if User_Input == selfResponse:
    print("Im good, how about yourself? ")
  else:
    print("Type again")

desire()

# This function obtain audio from microphone
"""
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
"""


# will need to make microphone work and computer say "print("Welcome fellow humans.")"
