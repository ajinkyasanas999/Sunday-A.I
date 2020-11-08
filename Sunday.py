import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import time
import os
import time 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.setProperty('rate', rate-28)
    engine.setProperty('volume', volume+0.100)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def get_audio():
    r = sr.Recognizer()
    print("Listening....")
    speak("Listening to you sir")

    with sr.Microphone() as source:
        
        audio_data = r.listen(source)
        print("Recognizing......")
        speak("Recognizing")

        try:
            text = r.recognize_google(audio_data)
            print(text)
        except:
            print("can't recognize....")
            speak("'can't recognize")
            get_audio()

        if "open code" in text:
            codePath = "C:\\Users\\SHREE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")
            time.sleep(15)

        if "open YouTube" in text:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/?gl=IN&tab=r1")
            time.sleep(15)

        if "open WhatsApp" in text:
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com")
            time.sleep(15)

        if "open Google" in text:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            time.sleep(15)

        if "time" in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is, {strTime}")

        if "who are you" in text:
            speak("I am Sunday, I am programmed by Ajinkya Sanas")

        if 'Wikipedia' in text or 'wikipedia' in text:
            speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=8)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if "Hello" in text or "hello" in text:
            speak("Hi sir")

        if "Hai" in text or "hai" in text:
            speak("Hello sir")

        if "Alexa" in text:
            speak("I am not Alexa of Google, nor Jarvis of Mark Zucherbug ,but I am Sunday of Ajinkya Sanas")

        if "Jarvis" in text:
            speak("I am not Jarvis of Mark Zucherbug, nor Alexa of Google ,but I am Sunday of Ajinkya Sanas")

        if "where are you" in text:
            speak("I'm stucked in Ajinkya's laptop, help me to come out")

        if "what is your name" in text:
            speak("My name is Sunday")      

        if "thank you" in text:
            speak("Ohhh! It's my job.") 

if __name__ == "__main__":
    wishMe()
    while True:
        get_audio()
