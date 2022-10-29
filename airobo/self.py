#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import datetime

print("Welcome Humans.")

self_memory = input("Please enter your message here: ")

UserInput = ("Hi")

"""
def desire():
  if self_response == UserInput:
    print("Im good, how about yourself? ")
  if self_response == UserInput2:
    print("Hello")
  else:
    print("I'm sorry, please try again.")

desire()
"""

class SelfResponse:
  def __init__(self, response):
    self.response = response
  
  if self_memory == UserInput:
    print("Hello there, how are you?")
  else:
    print("Try again")

R1 = SelfResponse(UserInput)

print(R1.response)

    
# will need to make computer response using speech
