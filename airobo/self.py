#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

print("Welcome!")

input_user = input("Say something: ")

engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

speak("Hello, user!")

