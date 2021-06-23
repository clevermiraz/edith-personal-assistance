import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #female voice


def speak(audio):
    '''engine can speak and answer my question'''

    engine.say(audio)
    engine.runAndWait()


def wishMe():
    ''' 
    what is time now then edith wish me and say how she can help me.

    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("Hello sir, I am Edith I Love you sir! how may I help you!")


def takeCommand():
    ''' it takes microphone input from user and return as string'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        # r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query} \n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accroding to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = "F:\\MEMORY\\song"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "open vs code" in query:
            vscode_dir = "C:\\Users\\Miraz\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(vscode_dir)

        elif "send email" in query:
            try:
                speak("what should i say? sir")
                content = takeCommand()
                to = "miraz.onesoft@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("sorry sir i'm not able to send your email! but I Love You sir")
