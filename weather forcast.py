import pyttsx3
import requests
import json

print("Welcome to Weather Application 1.O Created by Aryan !!")
s = pyttsx3.init()
while True:
    city = input("Enter city: ")
    try:
        if city == "exit":
            s.say("Thank you .. Have a nice day")
            s.runAndWait()
            break
        url = f"https://api.weatherapi.com/v1/current.json?key=887b9eb6bddf44d688d133837230310&q={city}"
        r = requests.get(url)
        wdic = json.loads(r.text)
        temp = wdic["current"]["temp_c"]
        f1 = f"The current weather in {city} is {temp}"
        print(f1)
        
        # rate = engine.getProperty('rate')
        s.setProperty('rate', 150)
        voices = s.getProperty('voices')
        s.setProperty('voice', voices[1].id)
        s.say(f1)
        s.runAndWait()
    except:
        print("Some error occured ")
