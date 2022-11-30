#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
# import wolframalpha
# import datetime

print("Welcome!")

input_user = input("Say something: ")

engine = pyttsx3.init()
GivenSpeech = "I’m increasingly inclined to think that there should be some regulatory oversight, maybe at the national and international level, just to make sure that we don’t do something very foolish. I mean with artificial intelligence we’re summoning the demon"

def speak(text):
  engine.say(text)
  engine.runAndWait()

rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate", 180)

speak(GivenSpeech) # say these words slower

# not too sure what to add tbh
