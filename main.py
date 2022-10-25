import psutil as psutil
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests
import randfacts

import spellWord
from jokes import jokes
from news import news
#import playsound


print('Loading your AI personal assistant.....')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[0].id)

def play_activation_sound():
# utils_dir = os.path.dirname(__file__)
    # activation_soundfile = os.path.join(utils_dir, '..', 'files', 'activation_sound.wav')
    # playsound(activation_soundfile)
    file = "activation_sound.wav"
    os.system(file)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-US')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Sorry, please say that again")
            return "None"
        return statement


speak("Your AI assitant speaking.......")
wishMe()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        text = takeCommand().lower()

        if text == 0:
            continue

        if "good bye" in text or "ok bye" in text or "stop" in text:
            speak('Good bye')
            print('Good bye')
            break

        if 'wikipedia' in text:
            speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open youtube' in text:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open gmail' in text:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in text:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in celsius unit is " +
                      str(round(current_temperature - 273)) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(round(current_temperature - 273)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in text or 'what can you do' in text:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in text or "who created you" in text or "who discovered you" in text:
            speak("I was built by Amir")
            print("I was built by Amir")

        elif "open stackoverflow" in text:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in text:
            print('Here are some headlines for you, Happy reading')
            speak('Here are some headlines for you, Happy reading')
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

            time.sleep(6)

        elif "camera" in text or "take a photo" in text:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'ask' in text:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        # elif "fact" or "facts" in statement:
        #    x = randfacts.getFact()
        #    print(x)
        #   speak("Did you know that " + x)

        elif "joke" or "jokes" in text:

            url = "https://official-joke-api.appspot.com/random_ten"

            a = jokes(url)

            for i in (a):
                print(i["setup"])
                speak(i["setup"])
                print(i["punchline"], "\n")
                speak(i["punchline"])

        elif "memory" in text:
            pid = os.getpid()
            py = psutil.Process(pid)
            memoryUse = py.memory_info()[0] / 2. **30
            print("I use {0:.2f} GB..".format(memoryUse))
            speak("I use {0:.2f} GB..".format(memoryUse))

        #elif "internet" and "speed" in text:

        elif "spell" in text:





        #elif "log off" or "sign out" in text:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
         #   subprocess.call(["shutdown", "/l"])

time.sleep(3)
