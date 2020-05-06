# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:43:29 2020

@author: VEENA
"""
import time
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
command= "please speak"
faf = "(1) Only Canadians and American call football as soccer.(2) Football is the most played sports on Earth (3) Football was invented in China in 476 BCE"
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

"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   

"""VOLUME"""
volume = engine.getProperty('rate')
engine.setProperty('volume', 2.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
while True :
    if 'histroy' in text or 'h' in text:
        engine.say("Football is a game which was also play earlier . Earlier,in 476 BC ,Football was invented in China . Football was Invented also in Greece,Rome and parts of Centeral America,years later . In 12th century,football was developed in England . On 16th century,an equavalent was played in Florence where it was called Calcio . In 1876,in paris,france,a football match was played . Earlier,this game was causing damage and death . It would be forbidden again in 1835,but at this stage the game had  been played in public school and years later,the rules were  change to perfect rules .")
        engine.runAndWait()
    if 'football' in text or 'Football' in text:
        engine.say("football is a game played in Euroupe majorly since 476 BCE in China .")
        engine.runAndWait()                
    if 'facts about  football' in text or 'faf' in text:        
        engine.say(faf)
    if "What is the fifa world cup ? " in text or "A" in text :
            print("the FIFA World Cup,often simply called the World Cup,is an internation association football competition .")
            engine.say("the FIFA World Cup,often simply called the World Cup,is an internation association football competition contested by the senior men`s national team of the members of the F`ed`eration Internatiale de Football Association(FIFA) .")
            engine.runAndWait()
    if  'Alexa,What does goalkeeper do ?' in text or 'gr' in text :
            print("goalkeeper protects the goal ")
            engine.say("goalkeeper protects the goal ")
            engine.runAndWait() 
    if "alexa,how many players are there in each team" in text or "tm" in text :
            print("11")
            engine.say("Each teams have 11 players . ")
            engine.runAndWait()     
    if "alexa,how many World Cups happen in fifa" in text or "Cups" in text :
            print("21 World Cup . ")
            engine.say("21 World Cup .")
            engine.runAndWait()
    if "alexa,which country won most FIFA World Cup?" in text or "tm" in text :
            print(" Brazil  . ")
            engine.say("Brazil won most FIFA World Cups (5).")
            engine.runAndWait()     
        
    if "alexa,who is the best goalkeeper in the world 2020?" in text or "2020" in text:
            print("Jan Oblak(OVR 90)  . ")
            engine.say("Jan Oblak(OVR 90) .")
            engine.runAndWait()  
    if "Who is the god of football" in text or "god" in text :
            print("Lionel Messi . ")
            engine.say("Lionel Messi from Arjentina .")
            engine.runAndWait()        
   
        
    if 'q' in text or 'quit' in text:
        print("closing")          