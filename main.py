import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('u19cs020@coed.svnit.ac.in', 'Anuj@123')
    server.sendmail('u19cs020@coed.svnit.ac.in', to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak("Good Morning master Anuj")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon master Anuj")
    else:
        speak("Good Evening master Anuj")
    speak("Hi ,I am Alfred, please tell me what can I do for you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()  # Converting user query into lower case
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening Youtube ')
            webbrowser.open("youtube.com")
        elif 'open amazon' in query:
            speak('Opening Amazon.in ')
            webbrowser.open("amazon.in")
        elif 'play music' in query:
            speak('Playing Music ')
            music_dir = 'C:\\Users\\acer\\OneDrive\\Documents\\songsad'
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))
            mixer.init()
            mixer.music.load('C:\\Users\\acer\\OneDrive\\Documents\\songsad\Illegal Weapon 2 - Street Dancer 3D.mp3')
            mixer.music.play()
        elif 'stop music' in query:
            mixer.music.stop()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open visual studio' in query:
            codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to' in query:
            try:
                speak("Sir, give me your message")
                print('Give message.......')
                content = takeCommand()
                to = "adarshdubey0803@gmail.com"
                sendEmail(to, content)
                print('Sending mail........')
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry master Anuj . I am not able to send this email")
        elif 'turn off' in query:
            speak('Good Bye Master Anuj')
            break
