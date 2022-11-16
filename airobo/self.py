#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
# import wikipedia
# import wolframalpha
# import datetime

print("Welcome!")

user1 = "Dota"

input_user = input("Say something: ")

engine = pyttsx3.init()
VoiceSpeed = 10
GivenSpeech = "Dota 2 is a 2013 multiplayer online battle arena video game by Valve. The game is a sequel to Defense of the Ancients, a community-created mod for Blizzard Entertainment's Warcraft III: Reign of Chaos."

def speak(text):
  engine.say(text)
  engine.setProperty('rate', VoiceSpeed)
  engine.runAndWait()

if GivenSpeech == user1:
  print(GivenSpeech)
else:
  print("Please try again") # fix this error

speak(GivenSpeech) # make this slower speed
