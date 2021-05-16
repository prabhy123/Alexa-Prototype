import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import streamlit as st

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass

    return command


def run_alexa():
    command1 = take_command()
    #print(command1)
    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        if 'AM'  in time:
            talk('Good morning Prabhakar')
        else:
            talk('Good evening Prabhakar')
    elif 'who is' or 'what is' in command1:
        person = command1.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command1:
        talk('sorry, I have a headache')
    elif 'are you single' in command1:
        talk('I am in a relationship with wifi')
    elif 'joke' in command1:
        talk(pyjokes.get_joke())
    elif 'alarm' in command1:
        talk("Your alarm is set")
    elif 'stop' in command1:
        print("Stopped")
        quit()
    else:
        talk('May be you are too intelligent!, Please say the command again.')

while True:
    run_alexa()

st.title("Alexa Prototype")
#st.audio(run_alexa)
