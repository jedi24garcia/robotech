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
# from pocketsphinx import LiveSpeech -- python 3.11 is completely unsupported.
# Meaning you will have to downgrade to 3.10 to use this module --

"""
password = "admiral"

while True:
  user_input = input("Please enter password: ")
  if user_input == password:
    break
  else:
    print("Wrong! Please try again!")
"""
   
# print("Hello there user, I will be your assistant for today.") -- will remove line at some point --
newVoiceRate = 170

engine = pyttsx3.init()
engine.setProperty("voice", "voice[1].id")
engine.setProperty("rate", newVoiceRate)

def speak(text):
  engine.say(text)
  engine.runAndWait()

# depending on the time, computer will say greetings below:
def wishGreetings():
  hour=datetime.datetime.now().hour    
  if hour>=0 and hour<12:
    speak("Good Morning!")
    print("Good Morning!")
  elif hour>=12 and hour<18:
    speak("Good Afternoon!")
    print("Good Afternoon!")
  else:
    speak("Good Evening!") 
    print("Good Evening!")

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
      print("I beg your pardon?")
      return "None"
    return statement
  
print("Hello there user, I will be your assistant for today.")
speak("Hello there user, I will be your assistant for today.")
wishGreetings()

if __name__ == "__main__":

  while True:
    speak("How can I help?")
    print("How can I help?")
    statement = TakeCommands().lower()
    if statement == 0:
      continue
    
    if "Ok bye" in statement or "stop" in statement:
      speak("Goodbye now")
      print("Goodbye now")
      break

    if "Ok, you can stop now" in statement:
      speak("Signing off")
      print("Signing off")
      break

    elif "search" in statement:
      statement = statement.replace("search", "")
      webbrowser.open_new_tab(statement)
      time.sleep(3)

# At this point, different sites will be added  

# We're going to add if statement here soon

    elif "open twitch" in statement:
      webbrowser.open_new_tab("https://www.twitch.tv/")
      speak("Here you go, twitch is now open.")
      print("Here you go, twitch is now open.")
      time.sleep(3)

    elif "open youtube" in statement:
      webbrowser.open_new_tab("https://www.youtube.com/")
      speak("Sweet as, here is youtube.")
      print("Sweet as, here is youtube.")
      time.sleep(3)

    elif "open linkedin" in statement:
      webbrowser.open_new_tab("https://www.linkedin.com/")
      speak("Really, this? Well, here you go then.")
      print("Really, this? Well, here you go then.")
      time.sleep(3)

    elif "open google" in statement:
      webbrowser.open_new_tab("https://www.google.com/")
      speak("Now opening google.")
      print("Now opening google.")
      time.sleep(3)

# End!

    elif "Logging off now" in statement or "signing out" in statement:
      speak("Okay, terminating machine now")
      subprocess.call(["Shutdown"])

time.sleep(5)
