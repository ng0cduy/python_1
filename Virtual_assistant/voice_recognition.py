import speech_recognition as sr

assistant_ear = sr.Recognizer()
with sr.Microphone() as mic:
    print ("I am listenning")
    audio = assistant_ear.listen(mic)
try:
    you = assistant_ear.recognize_google(audio)
except:
    you = "test"
print ("You: "+you)