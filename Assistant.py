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
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use desired voice index
engine.setProperty('rate', 150)  # Adjust speech rate

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000  # Adjust for ambient noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            speak("Anything else I can help you with?")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak("I didn't catch that. Please repeat.")
        return "none"
    except sr.RequestError:
        speak("Service is unavailable right now.")
        return "none"
    return query.lower()

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now().strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good morning, it's {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon, it's {tt}")
    else:
        speak(f"Good evening, it's {tt}")
    speak("How can I assist you today?")

def send_email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email', 'your_password')
        server.sendmail('your_email', to, content)
        server.close()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. Error: {e}")

def get_weather(city):
    try:
        api_key = "your_openweather_api_key"
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(base_url)
        data = response.json()
        if data['cod'] != '404':
            weather_info = data['main']
            temperature = weather_info['temp'] - 273.15  # Convert to Celsius
            weather_desc = data['weather'][0]['description']
            speak(f"The temperature in {city} is {temperature:.2f} degrees Celsius with {weather_desc}.")
        else:
            speak("City not found.")
    except Exception as e:
        speak(f"Error fetching weather: {e}")

def news():
    try:
        api_key = "your_news_api_key"
        main_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
        news_response = requests.get(main_url).json()
        articles = news_response["articles"]
        top_5_articles = articles[:5]
        for i, article in enumerate(top_5_articles, 1):
            speak(f"News {i}: {article['title']}")
    except Exception as e:
        speak(f"Unable to fetch news: {e}")

def set_alarm(time_str):
    alarm_hour, alarm_minute = map(int, time_str.split(":"))
    while True:
        if (datetime.datetime.now().hour == alarm_hour and
                datetime.datetime.now().minute == alarm_minute):
            speak("Wake up! Your alarm is ringing.")
            break
        time.sleep(20)  # Check every 20 seconds to reduce CPU usage

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()

        # Greet
        if "hello" in query:
            speak("Hello! How can I assist you today?")

        # Weather Information
        elif "weather" in query:
            speak("Please name the city.")
            city = takecommand()
            if city != "none":
                get_weather(city)

        # Alarm
        elif "set alarm" in query:
            speak("Tell me the time to set the alarm (e.g., 07:30).")
            alarm_time = takecommand()
            if alarm_time != "none":
                set_alarm(alarm_time)

        # Open Apps or Websites
        elif "open notepad" in query:
            os.startfile("C:\\Windows\\System32\\notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open youtube" in query:
            speak("What should I search on YouTube?")
            cm = takecommand()
            if cm != "none":
                webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")

        elif "play song on youtube" in query:
            speak("Which song would you like to play?")
            song = takecommand()
            if song != "none":
                kit.playonyt(song)

        # System Commands
        elif "shutdown" in query:
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            os.system("shutdown /r /t 5")

        # Email
        elif "email" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                if content != "none":
                    speak("Who should I send the email to?")
                    to = "recipient@example.com"  # Replace with actual recipient email
                    send_email(to, content)
            except Exception as e:
                speak(f"Sorry, I couldn't send the email: {e}")

        # Jokes
        elif "tell me a joke" in query:
            speak(pyjokes.get_joke())

        # News
        elif "news" in query:
            speak("Fetching top news.")
            news()

        # Exit
        elif "no thanks" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            sys.exit()
