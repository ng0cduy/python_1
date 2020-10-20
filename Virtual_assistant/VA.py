import speech_recognition as sr
import pyttsx3
import datetime
import re 

while True:
    assistant_ear = sr.Recognizer()
    with sr.Microphone() as mic:
        assistant_ear.adjust_for_ambient_noise(mic)
        print ("I am listenning")
        audio = assistant_ear.listen(mic)
    try:
        you = assistant_ear.recognize_google(audio)
    except:
        you = ""
    print ("You: "+you)
    speech = you

    if speech == "":
        assistant_response =  "I can not hear you"
    elif "today" in speech:
        today = datetime.date.today()
        d2 = today.strftime("%B %d, %Y")
        assistant_response = d2
    elif "now" in speech or "Nao" in speech:
        now = datetime.datetime.now()
        current_time  = now.strftime("%H hours %M minutes %S seconds")
        assistant_response = current_time
    elif "hello" in speech:
        assistant_response = "Hello"
    else:
        assistant_response = "Sorry I dont Understand"
    print (assistant_response)
    robot_response = assistant_response
    robot_speech = pyttsx3.init()
    robot_speech.say(robot_response)
    robot_speech.runAndWait()