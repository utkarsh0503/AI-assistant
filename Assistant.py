import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
import pyautogui
import imaplib
import email
import requests
from bs4 import BeautifulSoup
import json 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Adjust the index based on the voice you prefer
engine.setProperty('rate', 50)  # Adjust speech rate here

def speak(audio):
    engine.say(audio)
    print(audio) 
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000  # Adjust energy threshold for ambient noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            speak("anything else I can help you with, Mr. Utkarsh?")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak("Mister Utkarsh, I don't understand that")
        return "none"
    except sr.RequestError:
        speak("the service is down.")
        return "none"
    except Exception as e:
        speak("EHH, their is issue with your voice? ")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now().strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good morning , it's {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon , it's {tt}")
    else:
        speak(f"Good evening Mr., it's {tt}")
    speak("So, what are we going to make today?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

def news():
    main_url = ''
    # Implement the news fetching functionality here

def get_location():
    try:
        response = get("http://ipinfo.io/")
        data = response.json()
        location = data["city"]
        speak(f"Your current location is {location}")
    except Exception as e:
        speak("Sorry, I am unable to find your location.")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        if "Godrej" in query:
            speak("Hello there!")
        elif "what's in the fridge" in query:
            speak("lemme' check i cannot see anything in the but but their are project out side")
        elif "gen" in query:
            speak("Boss anything else i can help u with.")
        elif "hello" in query:
            speak("Hi, how can I help you?")
        elif "hello" in query:
            speak("Hi, how can I help you?")
        elif "hello" in query:
            speak("Hi, how can I help you?")

        elif "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("Opening YouTube, Boss..")
            speak("Boss, what should I search on YouTube?")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")

        elif "open spotify" in query:
            speak("Opening Spotify, Boss..")
            webbrowser.open("https://www.spotify.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Overflow, Boss..")
            webbrowser.open("https://www.stackoverflow.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Overflow, Boss..")
            webbrowser.open("https://www.stackoverflow.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Overflow, Boss..")
            webbrowser.open("https://www.stackoverflow.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Overflow, Boss..")
            webbrowser.open("https://www.stackoverflow.com")

        elif "open my linkedin" in query:
            speak("Opening your LinkedIn, Boss..")
            webbrowser.open("https://www.linkedin.com/in/utkarsh-bisht-8b02a025b/")

        elif "open google" in query:
            speak("Opening Google, Boss..")
            speak("Boss, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif "send message on whatsapp" in query:
            try:
                speak("Boss, to whom should I send the message?")
                number = takecommand().lower().replace(" ", "").replace("-", "")
                if not number.isdigit() or len(number) != 10:
                    speak("The number you provided is not valid. Please provide a 10-digit phone number.")
                else:
                    speak("What is the message?")
                    message = takecommand().lower()
                    
                    kit.sendwhatmsg_instantly(f"+91{number}", message)
                    time.sleep(10)  # Shorter wait to confirm message sending
                    speak("Message has been sent, Boss")
            except Exception as e:
                speak(f"An error occurred: {e}")

        elif "play song on youtube" in query:
            speak("Which song would you like to play?")
            song = takecommand().lower()
            kit.playonyt(song)

        elif "email to utkarsh" in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to, content)
                speak("Email has been sent to Utkarsh")
            except Exception as e:
                print(e)
                speak("Sorry sir, I'm not able to send this email")

        elif "no thanks" in query:
            speak("Okay Boss, get a girlfriend now because you are single.")
            sys.exit()

        elif "close notepad" in query:
            speak("Okay Boss, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close browser" in query or "close website" in query:
            speak("Closing the browser, Boss")
            pyautogui.hotkey("ctrl", "w")

        elif "close tab" in query:
            speak("Closing the tab, Boss")
            pyautogui.hotkey("ctrl", "w")

        elif "stop" in query:
            speak("bye Boss, find a new girlfriend cause you are single have a great day!")
            sys.exit()

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:

                speak("Boss, it's time")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "today news" in query:
            speak("Fetching today's news")
            news()

        elif "send a file" in query:
            email = 'utkarshbisht005@gmail.com'  # your mail id
            password = 'your_pass'  # account

