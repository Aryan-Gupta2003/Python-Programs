import pyttsx3
print("Welcome to RoboSpeaker 1.0 Created by Aryan")
a = pyttsx3.init()
while True:
    x = input("Enter command: ")
    if x == "exit":
        a.say("bye bye friend..see you soon")
        a.runAndWait()
        break
    # rate = engine.getProperty('rate')
    a.setProperty('rate', 150)
    voices = a.getProperty('voices')
    a.setProperty('voice', voices[0].id)
    #index 0 is for man voice and 1 for woman voice
    a.say(x)
    a.runAndWait()
