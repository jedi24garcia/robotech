#!/usr/bin/env python3

import speech_recognition as sr  # version updated to 3.10.0
import pyttsx3
import wikipedia
import datetime
import pyaudio
import time 
import sys
import subprocess
import webbrowser

class SelfAssistant:
  def __init__(self):
        self.newVoiceRate = 170
        self.engine = pyttsx3.init()
        self.engine.setProperty("voice", "voice[1].id")
        self.engine.setProperty("rate", self.newVoiceRate)

        self.speak("Hello there user, I will be your assistant for today.")  
        print(f"Hello there user, I will be your assistant for today.")
        self.wishGreetings()

  def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

  # depending on the time, computer will say greetings below:
  def wishGreetings(self):
    hour=datetime.datetime.now().hour    
    if hour>=0 and hour<12:
      self.speak("Good Morning!")
      print(f"Good Morning!")
    elif hour>=12 and hour<18:
      self.speak("Good Afternoon!")
      print(f"Good Afternoon!")
    else:
      self.speak("Good Evening!") 
      print(f"Good Evening!")

  def TakeCommands(self):
    path = "C:/Program Files (8x6)/Google/Chrome/Application/chrome.exe %s"
    r = sr.Recognizer()
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source, duration=0.5) # method reads the first second of the file stream and calibrates the recognizer to the noise level of the audio
      print("Listening... Say things like:")
      audio = r.listen(source)
    
      try:
        statement = r.recognize_google(audio,language='en-in')
        print(f"user said: {statement}\n")

      except Exception as e:
        self.speak("I beg your pardon?")
        print(f"I beg your pardon?")
        return "None"
      return statement
    

if __name__ == "__main__":
      assistant = SelfAssistant()

      def Perform(self):
        while True:
          self.speak("How can I help?")
          print(f"How can I help?")
          statement = self.TakeCommands().lower()
          if statement == 0:
            continue  
          
          if "Ok bye" in statement or "terminate" in statement or "stop" in statement:
            self.speak("Goodbye now")
            print(f"Goodbye now")
            break      
        
          elif "search" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)

      # At this point, different sites will be added  
      # We're going to add if statement here soon

          elif "What can you do" in statement or "Who made you?" in statement:
            self.speak("I am sir Jedi's personal assistant. As of now, I am terribly weak as I am just starting to learn how to be human.")
            print(f"I am sir Jedi's personal assistant. As of now, I am terribly weak as I am just starting to learn how to be human.")
      #    time.sleep(3)

          elif "open facebook" in statement:
            webbrowser.open_new_tab("https://www.facebook.com/")
            self.speak("Facebook is now open")
            print(f"Facebook is now open")
            time.sleep(3)

          elif "open twitch" in statement:
            webbrowser.open_new_tab("https://www.twitch.tv/")
            self.speak("Here you go, twitch is now open.")
            print(f"Here you go, twitch is now open.")
            time.sleep(3)

          elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com/")
            self.speak("Now open.")
            print(f"Now open.")
            time.sleep(3)
            
          elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com/")
            self.speak("Sweet as, here is youtube.")
            print(f"Sweet as, here is youtube.")
            time.sleep(3)

          elif "open linkedin" in statement:
            webbrowser.open_new_tab("https://www.linkedin.com/")
            self.speak("Really, this? Well, here you go then.")
            print(f"Really, this? Well, here you go then.")
            time.sleep(3)

          elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com/")
            self.speak("Now opening google.")
            print(f"Now opening google.")
            time.sleep(3)

          elif "open netflix" in statement:
            webbrowser.open_new_tab("https://www.netflix.com/nz/")
            self.speak("Right away.")
            print(f"Right away.")
            time.sleep(3)

          elif "open disneyplus" in statement:
            webbrowser.open_new_tab("https://www.disneyplus.com/en-nz/")
            self.speak("You got it.")
            print(f"You got it.")
            time.sleep(3)

          elif "open prime" in statement:
            webbrowser.open_new_tab("https://www.primevideo.com/")
            self.speak("Prime is now open.")
            print(f"Prime is now open.")
            time.sleep(3)

          elif "open discord" in statement:
            webbrowser.open_new_tab("https://discord.com/")
            self.speak("Discord is now open")
            print(f"Discord is now open")
            time.sleep(3)
          
          elif "Logging off now" in statement or "Signing out" in statement or "Terminate" in statement:
            self.speak("Very well, terminating machine now.")
            print(f"Very well, terminating machine now.")
            subprocess.call(["Shutdown", "/l", "5"])

time.sleep(5)