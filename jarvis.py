import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    
    speak("Jarvis is at your service, Please Let me know how may i help you ")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print("e")
        
        print("Say that again please...")
        return "None"
    return query
# end def

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmal.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
# end def

if __name__ == "__main__":
    #speak("hello shruti")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
    
    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
      
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")   
        
    elif 'open spotify' in query:
        webbrowser.open("spotify.com")
        
    elif 'play music' in query:
        music_dir = 'C:\\Users\\Dipak Kamble\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is (strTime)")
        
    #elif 'open code' in query:
        #codePath = "C:\\Users\Dipak Kamble\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #os.startfile(codePath)
        
    elif 'email to shruti' in query:
        try:
            speak("What should i say?")
            content = takeCommand()
            to = "learningshru17@gmal.com"
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry i couldn't send the email")

