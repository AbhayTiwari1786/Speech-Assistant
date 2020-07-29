import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os 
import smtplib
import webbrowser
import pyaudio
#import vlc
#import random
#import simpleaudio as sa
from playsound import playsound


MASTER = "Abhay"

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


# speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
# this function will wish you as per the current time
def wishMe():

    hour = int(datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<16:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    
    #speak("Iam Meenakshi......How may I help you ??")
#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2)as source:
        print("Listening...!!!")
        audio = r.listen(source)

    try :
        print("Recognizing...!!!")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said:- {query}\n")

    except Exception as e:
        print("Sorry...say that again please....!!!",e)
        query = None
    
    return query


# Main program starts here
#speak("Initialising.... Meenakshi...")
wishMe()
query = takeCommand()

# logic for executing tasks as per the query

if 'wikipedia' in query.lower():
    speak('Searching wikipedia.....!!!')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.open("google.com")

elif 'open gmail' in query.lower():
    webbrowser.open("gmail.com")

elif 'play music' in query.lower():
    # path="//home//abhaytiwari1786//Music//"
    # files = os.listdir(path)
    # d = random.choice(files)
    # os.system('//home//abhaytiwari1786//Music//' + d)
    playsound('//home//abhaytiwari1786//Music/1.wav')

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}") 
    print(strTime)

elif 'open code' in query.lower():
    codePath = "/usr/bin/code"
    os.system(codePath)