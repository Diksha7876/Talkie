import pyttsx3
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import os
import time
import pyautogui
import pyjokes
import pywhatkit
import random
import sounddevice 
# from scipy.io.wavfile import write


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)                # '0' for male and '1' for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("heyy Diksha")

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<16:
        speak('Good Afternoon')
    else:
        speak('Good evening')
# wishme()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print('Recording...')
        query=r.recognize_google(audio,language='en-in')
        print(f'Usercommand is {query}')
    except Exception as a:
        print(a)
        print('Say Again')
        return 'none'
    return query

if __name__=='__main__':
    wishme()
    speak('heloo')
    while True:
        query=takecommand().lower()
        if 'open google' in query:
            webbrowser.open('https://www.google.com/')
        elif 'how are you' in query:
            speak('Like you are')
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        elif 'wikipedia' in query:
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=10)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open notepad' in query:
            speak("opening notepad")
            p='C:\\Windows\\notepad.exe'
            os.startfile(p)
        elif 'open google chrome' in query:
            speak("opening google chrome")
            p="C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(p)
        elif 'current time' in query:
            speak(time.strftime("%H %M %S %p"))
        elif 'volume up' in query:
            speak("ok")
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            speak("ok")
            pyautogui.press("volumedown")
        elif 'mute' in query:
            speak("ok")
            pyautogui.press("volumemute")
        elif 'unmute' in query:
            speak("ok")
            pyautogui.press("volumeunmute")
        elif 'jokes' in query:
            speak(pyjokes.get_jokes())
            print(pyjokes.get_jokes())
        elif 'play song'in query:
            speak("playing...")
            song=query.replace("play song","")
            pywhatkit.playonyt(song)
        elif "toss a coin" in query:
            a=["head","tail"]
            result=random.choice(a)
            print(f'the computer choose{result}')
            speak(f'the computer choose {result}')
        elif "increase brightness" in query:
            speak("ok")
            pyautogui.press("F5")
        elif 'exit' in query:
            speak('Byy mam')
            exit()
        else:
            speak('Byy Sir')
            exit()