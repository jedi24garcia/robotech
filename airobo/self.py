#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import datetime

print("Welcome humans.")

self_response  = input("Please enter your message here: ")

UserInput = ("How are you?")
UserInput2 = ("Hi")


def desire():
  if self_response == UserInput:
    print("Im good, how about yourself? ")
  if self_response == UserInput2:
    print("Hello")
  else:
    print("I'm sorry, please try again.")

desire()



# will need to make computer response using speech
