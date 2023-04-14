#!/usr/bin/env python3

" We will be running this program through Windows "

import speech_recognition as sr  # version updated to 3.10.0
import pyttsx3
import wikipedia
import datetime
import pyaudio
import time 
import sys
import subprocess
import webbrowser
import tkinter as tk
from tkinter import *

print("Hint: The Admiral of the mighty Claddish Navy.")

self_password = "Kunkka"
newVoiceRate = 170

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", newVoiceRate)

"""
# will place tkinter here for the GUI
window = tk.Tk()
window.title("Ad Astra")
window.geometry("800x500+50+50")
window.configure(bg="black")
window.attributes("-topmost", 1)
"""

def speak(text):
  engine.say(text)
  engine.runAndWait()

# password
while True:
  speak("Please enter password here: ")
  UserInput = input("Please enter password here: ")
  if UserInput == self_password:
    speak("Access Granted.")
    print("Access Granted.")
    break
  else:
      speak("Incorrect password, noob please try again.")
      print(f"Incorrect password, noob please try again.")

# depending on the time, computer will say greetings below:
def wishGreetings():
  hour=datetime.datetime.now().hour    
  if hour>=0 and hour<12:
    speak("Good Morning!")
    print(f"Good Morning!")
  elif hour>=12 and hour<18:
    speak("Good Afternoon!")
    print(f"Good Afternoon!")
  else:
    speak("Good Evening!") 
    print(f"Good Evening!")

def TakeCommands():
  path = "C:/Program Files (8x6)/Google/Chrome/Application/chrome.exe %s"
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.5) # method reads the first second of the file stream and calibrates the recognizer to the noise level of the audio
    print("Listening...")
    audio = r.listen(source)
  
    try:
      statement = r.recognize_google(audio,language='en-in')
       # for phrase in LiveSpeech(): -- will add once Python 3.11 supports this module
      print(f"user said: {statement}\n")

    except Exception as e:
      speak("I beg your pardon?")
      print(f"I beg your pardon?")
      return "None"
    return statement

speak("Hello there user, I will be your assistant for today.")  
print(f"Hello there user, I will be your assistant for today.")
wishGreetings()
# window.mainloop() # not working at the moment

if __name__ == "__main__":

  while True:
    speak("How can I help?")
    print(f"How can I help?")
    statement = TakeCommands().lower()
    if statement == 0:
      continue  
    
    if "Ok bye" in statement or "terminate" in statement or "stop" in statement:
      speak("Goodbye now")
      print(f"Goodbye now")
      break      
   
    elif "search" in statement:
      statement = statement.replace("search", "")
      webbrowser.open_new_tab(statement)
      time.sleep(3)

# At this point, different sites will be added  
# We're going to add if statement here soon

    elif "What can you do" in statement or "Who made you?" in statement:
      speak("I am sir Jedi's personal assistant. As of now, I am terribly weak as I am just starting to learn how to be human.")
  #   print(f"I am sir Jedi's personal assistant. As of now, I am terribly weak as I am just starting to learn how to be human.")
  #   time.sleep(3)

    elif "open facebook" in statement:
      webbrowser.open_new_tab("https://www.facebook.com/")
      speak("Facebook is now open")
      print(f"Facebook is now open")
      time.sleep(3)

    elif "open twitch" in statement:
      webbrowser.open_new_tab("https://www.twitch.tv/")
      speak("Here you go, twitch is now open.")
      print(f"Here you go, twitch is now open.")
      time.sleep(3)

    elif "open github" in statement:
      webbrowser.open_new_tab("https://github.com/")
      speak("Now open")
      print(f"Now open")
      time.sleep(3)
      
    elif "open youtube" in statement:
      webbrowser.open_new_tab("https://www.youtube.com/")
      speak("Sweet as, here is youtube.")
      print(f"Sweet as, here is youtube.")
      time.sleep(3)

    elif "open linkedin" in statement:
      webbrowser.open_new_tab("https://www.linkedin.com/")
      speak("Really, this? Well, here you go then.")
      print(f"Really, this? Well, here you go then.")
      time.sleep(3)

    elif "open google" in statement:
      webbrowser.open_new_tab("https://www.google.com/")
      speak("Now opening google.")
      print(f"Now opening google.")
      time.sleep(3)

    elif "open netflix" in statement:
      webbrowser.open_new_tab("https://www.netflix.com/nz/")
      speak("Right away")
      print(f"Right away")
      time.sleep(3)

    elif "open disneyplus" in statement:
      webbrowser.open_new_tab("https://www.disneyplus.com/en-nz/")
      speak("You got it")
      print(f"You got it")
      time.sleep(3)

    elif "open prime" in statement:
      webbrowser.open_new_tab("https://www.primevideo.com/")
      speak("Prime is now open")
      print(f"Prime is now open")
      time.sleep(3)

    # api for weather here
    # api_key="8ef61edcf1c576d65d836254e11ea420"

# enter weather here using "8ef61edcf1c576d65d836254e11ea420"
    
    # End!

    elif "Logging off now" in statement or "Signing out" in statement or "Terminate system" in statement:
      speak("Very well, terminating machine now")
      print("Very well, terminating machine now")
      subprocess.call(["Shutdown", "/1"])

time.sleep(5)