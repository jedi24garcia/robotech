#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
#import comtypes

print("Welcome fellow humans.") #sample response

r = sr.Recognizer()
r = sr.Microphone()

class SelfSpeak():
  def __init__(self, speak):
    self = speak

'''time.sleeps(3)'''
