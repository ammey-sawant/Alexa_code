# Alexa_code
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:59:35 2020

@author: VEENA
"""
import time
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
command= "please speak"
"""Rate"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)


"""VOLUME"""
volume = engine.getProperty('rate')
engine.setProperty('volume', 2.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
    
r = sr.Recognizer()
engine.say(command)
engine.runAndWait()
time.sleep(1)
with sr.Microphone() as source:
     print("Speak")
     r.energy_threshold = 5000
     r.adjust_for_ambient_noise(source, duration=3)
     audio = r.listen(source, timeout = 19)

try:
    text= r.recognize_google(audio)
    time.sleep(1)
    print("you said :",format(text))
    engine.say("you said :" + str(text))
    engine.runAndWait()
except:
    print("ListenError : Could`nt hear your audio")
   
